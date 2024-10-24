from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50,default='')
    email=models.EmailField(max_length=50,default='')
    subject= models.CharField(max_length=100,default='')
    message=models.TextField(max_length=500,default='')
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.subject}'
