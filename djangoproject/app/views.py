from django.shortcuts import render
from .models import application
from django.shortcuts import get_object_or_404

# Create your views here.
def app(request):
    cha = application.objects.all()
    return render(request,'app/app.html', {'cha': cha})

def cha_details(request,chai_id):
    chai = get_object_or_404(application, pk=chai_id)
    return render(request,'app/cha_details.html',{'chai':chai})