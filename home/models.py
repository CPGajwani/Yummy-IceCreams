from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self) -> str:
        return self.name