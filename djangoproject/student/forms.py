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
    ('Mymenshing','Mymenshing'),
    ('Barishal','Barishal'),
    ('Narshingdi','Narshingdi'),
    ('Madaripur','Madaripur'),
    ('Noagaon','Noahgaon'),
    ('Nator','Nator'),
    ('Narayanganj','Narayanganj'),
    ('Rajshahi','Rajshahi'),
    ('Sylhet','Sylhet'),
    ('Coxs Bazar','Coxs Bazar'),

)

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=gender_choice,
        widget=forms.RadioSelect,
    )

    job_city = forms.MultipleChoiceField(              #use MultipleChoiceField to select multiple option but in vertically like select option
        choices=job_city_choice,
        widget=forms.CheckboxSelectMultiple,            #use CheckboxSelectMultiple to select multiple also but in a different way.(better)
        label ='Prefered Job Cities:',
        help_text='Select One or More cities where you prefer to work'
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
            'Zilla': forms.Select(attrs={'class':'form-select'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your 11 digit Mobile Number'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email address'}),

        }

