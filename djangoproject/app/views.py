from django.shortcuts import render
from .models import Cha,store
from django.shortcuts import get_object_or_404
from .forms import ChaForm

# Create your views here.
def app(request):
    cha = Cha.objects.all()
    return render(request,'app/app.html', {'cha': cha})

def cha_details(request,chai_id):
    chai = get_object_or_404(Cha, pk=chai_id)
    return render(request,'app/cha_details.html',{'chai':chai})

def cha_store(request):
    stores = None

    if request.method == 'POST':
        form = ChaForm(request.POST) 
        if form.is_valid():
            cha_var = form.cleaned_data['cha'] 
            stores = store.objects.filter(cha_varieties = cha_var)
    
    else:
        form = ChaForm()



    return render(request, 'app/cha_store.html',{'stores': stores, 'form': form})