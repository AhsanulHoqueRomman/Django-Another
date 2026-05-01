from django.shortcuts import render
from .models import Profile
from student.forms import ProfileForm

# Create your views here.

def home (request):
    form = ProfileForm()
    return render(request, 'student/home.html',{'form': form})