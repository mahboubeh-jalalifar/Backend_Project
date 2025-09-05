from django.db import models
from django.contrib.auth.models import AbstractUser

class Roles (models.TextChoices):
       Admin= "Admin","Admin",
       Empoyee= "Employee","Employee",
       Teacher=  "Teacher","Teacher",
       Student= "Student","Student",
       Parents= "Parents","Parents",
       Others= "Others","Others",
                   
class UserModel (AbstractUser):
    username= models.OneToOneField (max_length=50 , on_delete=models.CASCADE) # type: ignore
    role= models.CharField (max_length=50 , choices=Roles.choices , default=Roles.Admin)
    email= models.EmailField (max_length=200, unique=True )
    age= models.PositiveIntegerField (max_length=2)
    updated_at= models.DateTimeField (auto_now=True)
    created_at=models.DateTimeField (auto_now_add=True)
    def __str__ (self):
        return self.role
    



    


# Create your models here.
