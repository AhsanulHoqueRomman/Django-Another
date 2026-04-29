from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class application(models.Model):
    CHA_TYPE_CHOICE =[
        ('RC','Rong Cha'),
        ('DC','Dudh Cha'),
        ('MC','Masala Cha'),
        ('LC','Lebu Cha'),
        ('AC','Ada Cha'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    chaType = models.CharField(max_length=2,choices=CHA_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name



##One To Many Relationship model:

class chaReview(models.Model):

    rating_choice= [
        ('1','Very Low'),
        ('2','Low'),
        ('3','Medium'),
        ('4','Good'),
        ('5','Excellent')
    ]

    cha = models.ForeignKey(application, on_delete= models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(max_length=2, choices=rating_choice)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.cha.name}'
    


#Many to Many Relationship:

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cha_varieties = models.ManyToManyField(application, related_name='stores')

    def __str__(self):
        return self.name
    

#One to One

class chaCertificate(models.Model):
    chai = models.OneToOneField(application, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField

    def __str__(self):
        return f'Certificate for {self.name.chai}'
