from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Citizen(models.Model):
    mec_no = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name= models.CharField(max_length=20)
    phone= models.BigIntegerField(max_length=10)
    Guardian= models.ManyToManyField('Citizen', on_delete=models.CASCADE,related_name='guardians')
    Address=models.TextField(blank=True, null=True)
    skills= models.ManyToManyField('Skill', on_delete=models.CASCADE, related_name='skillset')
    
    def __str__(self):
        return self.name
    
class Institution(models.Model):
    Inst_id= models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=20)
    TYPE_CHOICES = (
    ("school", "School"),
    ("college", "College"),
    ("university", "University"),
    )
    type = models.CharField(max_length=9, choices=TYPE_CHOICES, default="school")
    location=models.CharField(max_length=15)
    Acc_status=models.CharField(max_length=5)                         