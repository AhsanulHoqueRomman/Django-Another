from django.shortcuts import render, redirect
from .models import Profile
from student.forms import ProfileForm

# Create your views here.

def home (request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')         #return to home.Previous data will not be shown again.
    else:
        form = ProfileForm()
    return render(request, 'student/home.html',{'form': form})