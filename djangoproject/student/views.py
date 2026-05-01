from django.shortcuts import render, redirect
from .models import Profile
from student.forms import ProfileForm

# Create your views here.

def home (request):
    candidates = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')         #return to home.Previous data will not be shown again.
    else:
        form = ProfileForm()
    return render(request, 'student/home.html',{'form': form, 'candidates': candidates})


def candidate_detail(request, id):
    candidates = Profile.objects.get(id = id)
    return render(request,'student/candidate.html', {'candidates':candidates})