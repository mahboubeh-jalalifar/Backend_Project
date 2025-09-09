from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from datetime import date


class Roles (models.TextChoices):
       Admin= "Admin","Admin",
       Empoyee= "Employee","Employee",
       Teacher=  "Teacher","Teacher",
       Student= "Student","Student",
       Parents= "Parents","Parents",
       Others= "Others","Others",

class Gender (models.TextChoices):
     Male= "Male","Male",
     Female= "Female","female",
     Other= "Other","Other",
                   
class UserModel (AbstractUser):
    role= models.CharField (max_length=50 , choices=Roles.choices , default=Roles.Student)
    email= models.EmailField (max_length=200, unique=True )
    national_id_number= models.CharField (unique=True, null= True , blank=True)
    phone=models.IntegerField (blank=True,null=True)
    adress=models.CharField(max_length=200,blank=True,null=True)
    date_of_birth= models.DateTimeField (blank=True,null=True)
    gender= models.CharField (choices=Gender.choices, null=True,blank=True)
    updated_at= models.DateTimeField (auto_now=True)
    created_at=models.DateTimeField (auto_now_add=True)

    @property
    def age(self):
        today = date.today()
        now = self.date_of_birth.date()
        return today.year - now.year - ((today.month, today.day) < (now.month, now.day))

    def __str__(self):
        return f"{self.username} is {self.role} and is {self.age} years old"

    



    


# Create your models here.
