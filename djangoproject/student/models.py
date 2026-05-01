from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('The Pin code must be 6 digits!')
    

Zilla_choice =(
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

# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveBigIntegerField(
        validators=[validate_pin_length],
        help_text='Enter 6-digit pin code')
    
    Zilla = models.CharField(choices=Zilla_choice, max_length=100)
    mobile = models.CharField(
        validators=[RegexValidator(regex=r'^\d{11}$')],
        max_length=11,
        help_text='Enter 11 digit mobile number'

    )
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)

