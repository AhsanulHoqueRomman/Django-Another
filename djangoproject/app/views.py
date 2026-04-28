from django.shortcuts import render
from .models import application
# Create your views here.
def app(request):
    cha = application.objects.all()
    return render(request,'app/app.html', {'cha': cha})