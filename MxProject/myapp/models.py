from django.db import models
from django.contrib.auth.models import User


class RegisterEmployee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = "RegisterEmp"
    