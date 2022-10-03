from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

ZODIAC_SIGNS = (
    ("Aries", "Aries"),
    ("Tauro", "Taurus"),
    ("Geminis", "Gemini"),
    ("Cancer", "Cancer"),
    ("Leo", "Leo"),
    ("Virgo", "Virgo"),
    ("Libra", "Libra"),
    ("Escorpio", "Escorpio"),
    ("Sagitario", "Sagitario"),
    ("Capricornio", "Capricornio"),
    ("Acuario", "Acuario"),
    ("Piscis", "Piscis"),
)

class InterestCategory(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

class Interest(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(InterestCategory,
    on_delete=models.CASCADE)

class ZodiacSign(models.Model):
    name = models.CharField(choices=ZODIAC_SIGNS, max_length=11)

class PoliticalView(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

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

class Question(models.Model):
    lang = models.CharField(max_length = 2)
    name = models.CharField(max_length=50)

class Instagram(models.Model):
    has_instagram = models.BooleanField(default= False)
    token = models.CharField(max_length=100)

class Spotify(models.Model):
    has_spotify = models.BooleanField(default= False)
    token = models.CharField(max_length=100)

class Municipio(models.Model):
    municipio = models.CharField(max_length=100)

class City(models.Model):
    ciudad = models.CharField(max_length=100)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default=None) 
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    interests = models.ManyToManyField(Interest, default=None)
    zodiac_sign = models.ManyToManyField(ZodiacSign, default=None)
    political_views = models.ManyToManyField(PoliticalView, default=None)
    # connections -> list of users
    height_in_cm = models.IntegerField(validators = [MaxValueValidator(220), MinValueValidator(99)], 
    default=0)
    workout = models.ManyToManyField(Workout, default=None)
    education = models.ManyToManyField(Education, default=None)
    drinking = models.ManyToManyField(Drinking, default=None)
    smoking = models.ManyToManyField(Smoking, default=None)
    gender = models.ManyToManyField(Gender, default=None)
    looking_for = models.ManyToManyField(LookingFor, default=None)
    kids = models.ManyToManyField(Kids, default=None)
    religion = models.ManyToManyField(Religion, default=None)
    languages = models.ManyToManyField(Languages, default=None)
    questions = models.ManyToManyField(Question, default=None)
    instagram = models.ManyToManyField(Instagram, default=None)
    spotify = models.ManyToManyField(Spotify, default=None)
    location = models.ForeignKey(City, default=None, on_delete=models.CASCADE)
    city_of_origin = models.ForeignKey(City, default=None, on_delete=models.CASCADE, related_name="city_origin")
    date_of_birth = models.DateField()
    is_paid_profile = models.BooleanField(default=False)
