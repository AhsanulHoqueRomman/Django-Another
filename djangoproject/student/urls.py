from django.urls import path
from student.views import home
from student import views


urlpatterns = [
    path('', views.home, name='home')
]
