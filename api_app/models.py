from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50) #Nullable
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    #interests -> enumerable
    #zodiac sign -> enumerable
    #political views -> enumerable
    #connections -> list of users
    date_of_birth = models.DateField()
    