from django.db import models
from django.utils import timezone

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
