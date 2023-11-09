from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=18)
    last_name = models.CharField(max_length=18)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(180)])
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
    

