from django import forms
from . import models
from student.models import Profile


gender_choice =(
    ('M','Male'),
    ('F','Female'),
    ('O','Others')
)

job_city_choice = (
    ('Dhaka','Dhaka'),
    ('Chittagong','Chittagong'),
    ('Cumilla','Cumilla'),
    ('Lakshmipur','Lakshmipur'),
    ('Noakhali','Noakhali'),
    ('Feni','Feni'),
    ('Chadpur','Chadpur'),
    ('Mymenshing','Mymenshing'),
    ('Bhola','Bhola'),
    ('Barishal','Barishal'),
    ('Patuakhali','Patuakhali'),
    ('Gazipur','Gazipur'),
    ('Narshingdi','Narshingdi'),
    ('Madaripur','Madaripur'),
    ('Noagaon','Noahgaon'),
    ('Pabna','Pabna'),
    ('Nator','Nator'),
    ('Narayanganj','Narayanganj'),
    ('Manikganj','Manikganj'),
    ('Rajshahi','Rajshahi'),
    ('Sylhet','Sylhet'),
    ('Coxs Bazar','Coxs Bazar'),

)

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=gender_choice,
        widget=forms.RadioSelect
    )
    class Meta:
        model = Profile
        fields = [
            'name','dob','gender','locality','city','pin','Zilla','mobile','email','job_city','profile_image','my_file'
        ]

        labels ={
            'name':'Full Name',
            'dob': 'Date Of Birth',
            'pin':'PIN Code',
            'mobile':'Mobile Number',
        }

        help_texts ={
            'profile_image' : 'Optional: Upload a Profile Image', 
            'my_file': 'Optional: Attach any additional Document(Pdf,DOCX,etc.)'
        }

        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id':'datepicker','type':'date'}),
            'locality': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your area name' }),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your city name' }),
            'pin': forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter 6 digit PIN code' }),
            'Zilla': forms.Select(attrs={'class':'form-select'})

        }

