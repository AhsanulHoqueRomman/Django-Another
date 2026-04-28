
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),        #localhost:8000/app
    path('<int:chai_id>/', views.cha_details, name='cha_details'),        
    
]