from django import forms
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
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

