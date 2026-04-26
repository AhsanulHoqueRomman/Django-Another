from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello,This is our Home page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello,This is our About page")
def contact(request):
    return HttpResponse("Hello,This is our Contact page")