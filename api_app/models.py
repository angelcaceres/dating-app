from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

class InterestCategory(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

class Interest(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(InterestCategory)

class ZodiacSign(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

class PoliticalView(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

class Zodiac_sign(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

class Workout(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Education(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Drinking(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Smoking(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Gender(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Kids(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class LookingFor(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Religion(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Languages(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default=None) 
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    interests = models.ManyToManyField(Interest, default=None)
    zodiac_sign = models.ForeignKey(ZodiacSign)
    political_views = models.ManyToManyField(PoliticalView, default=None)
    # connections -> list of users
    height_in_cm = models.IntegerField(max=220, min=99)
    workout = models.models.ManyToManyField(Workout, default=None)
    education = models.models.ManyToManyField(Education, default=None)
    drinking = models.models.ManyToManyField(Drinking, default=None)
    smoking = models.ManyToManyField(Smoking, default=None)
    gender = models.ManyToManyField(Gender, default=None)
    looking_for = models.ManyToManyField(LookingFor, default=None)
    kids = models.ManyToManyField(Kids, default=None)
    religion = models.ManyToManyField(Religion, default=None)
    languages = models.ManyToManyField(Languages, default=None)
    # questions -> enumerable -> answers using id as key
    # instagram
    # spotify
    # location -> maybe use maps api or something
    # city of origin
    date_of_birth = models.DateField()
    is_paid_profile = models.BooleanField(default=False)
