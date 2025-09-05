from models import UserModel
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User= get_user_model

class UserModelSerializer (serializers.Serializer):
     password = serializers.CharField  (write_only= True, null= True , blank= True)
     class meta:
        model= get_user_model
        fields = ["id","username","password","first_name","last_name","email","role","age"] 
        read_only_field = ["id"]
        
        def create (self,validated_data):
            password = validated_data.pop ("password")
            user = User.objects.create (
            username=validated_data ["username"],
            email= validated_data["email"],
              )
            validate_password(password,user)
            user.set_password (password)
            user.save()
            return User
        
        def update(self, instance, validated_data):
           password = validated_data.pop ("password")
           for key,value in validate_password.items():
            setattr (instance,key,value)
            if password:
             validate_password(instance,password)
            instance.set_password (password)
            instance.save ()
            return instance

