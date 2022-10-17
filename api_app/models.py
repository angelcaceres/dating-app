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

DRINKING_OPTIONS = (
    ("Compañia", "Sólo en compañía"),
    ("Nunca", "Nunca"),
    ("Con frecuencia", "Con frecuencia"),
    ("No bebo", "No bebo"),
)

INTEREST_OPTIONS = (
    ("Creatividad", "Creatividad"),
    ("Deportes", "Deportes"),
    ("Salidas", "Salidas"),
    ("Quedarse en casa", "Quedarse en casa"),
    ("Cine y televisión", "Cine y televisión"),
    ("Leer", "Leer"),
    ("Música", "Música"),
    ("Comida y bebida", "Comida y bebida"),
    ("Viajes", "Viajes"),
    ("Mascotas", "Mascotas"),
    ("Valores y personalidad", "Valores y personalidad"),
    ("Causas", "Causas"),
)

POLITICAL_VIEWS = (
    ("Sin interés", "Sin interés"),
    ("De centro", "De centro"),
    ("Izquierda", "Izquierda"),
    ("Derecha", "Derecha"),
    ("Socialista", "Socialista"),
)

WORKOUT_OPTIONS = (
    ("A menudo", "A menudo"),
    ("A veces", "A veces"),
    ("Casi nunca", "Casi nunca"),
)

EDUCATION_OPTIONS = (
    ("Preparatoria", "Preparatoria"),
    ("Formación profesional", "Formación profesional"),
    ("Estudiando una licenciatura", "Estudiando una licenciatura"),
    ("Bachillerato", "Bachillerato"),
    ("Estudiando un posgrado", "Estudiando un posgrado"),
    ("Posgrado", "Posgrado"),
)

SMOKING_OPTIONS = (
    ("Sólo en compañía", "Sólo en compañía"),
    ("Nunca", "Nunca"),
    ("Habitualmente", "Habitualmente"),
)

GENDER_OPTIONS = (
    ("Mujer", "Mujer"),
    ("Hombre", "Hombre"),
    ("No binario", "No binario"),
    ("Otro", "Otro"),
)

KIDS_OPTIONS = (
    ("Algún día", "Algún día"),
    ("No quiero", "No quiero"),
    ("Ya tengo y quiero mas", "Ya tengo y quiero mas"),
    ("Ya tengo y no quiero mas", "Ya tengo y no quiero mas"),
    ("Aún no se", "Aún no se"),
)

LOOKING_FOR_OPTIONS = (
    ("Relación", "Relación"),
    ("Nada serio", "Nada serio"),
    ("No lo se aún", "No lo se aún"),
    ("Matrimonio", "Matrimonio"),
)

RELIGION_OPTIONS = (
    ("Agnosticismo", "Agnosticismo"),
    ("Ateísmo", "Ateísmo"),
    ("Budismo", "Budismo"),
    ("Catolicismo", "Catolicismo"),
    ("Cristianismo", "Cristianismo"),
    ("Hinduismo", "Hinduismo"),
    ("Judaismo", "Judaismo"),
    ("Jainismo", "Jainismo"),
    ("Mormonismo", "Mormonismo"),
    ("Islam", "Islam"),
    ("Zoroastrismo", "Zoroastrismo"),
    ("Sijismo", "Sijismo"),
    ("Espiritual", "Espiritual"),
    ("Otra", "Otra"),
)


class InterestCategory(models.Model):
    lang = models.CharField(choices=INTEREST_OPTIONS, max_length=25)

class Interest(models.Model):
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(InterestCategory,
    on_delete=models.CASCADE)

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
    zodiac_sign = models.CharField(choices=ZODIAC_SIGNS, max_length=11, default=None)
    political_views = models.CharField(choices=POLITICAL_VIEWS, max_length=11, default=None)
    # connections -> list of users
    height_in_cm = models.IntegerField(validators = [MaxValueValidator(220), MinValueValidator(99)], 
    default=0)
    workout = models.CharField(choices=WORKOUT_OPTIONS, max_length=10, default=None)
    education = models.CharField(choices=EDUCATION_OPTIONS, max_length=27, default=None)
    drinking = models.CharField(choices=DRINKING_OPTIONS, max_length=16, default=None)
    smoking = models.CharField(choices=SMOKING_OPTIONS, max_length=16, default=None)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=10, default=None)
    looking_for = models.CharField(choices=LOOKING_FOR_OPTIONS, max_length=12, default=None)
    kids = models.CharField(choices=KIDS_OPTIONS, max_length=25, default=None)
    religion = models.CharField(choices=RELIGION_OPTIONS, max_length=12, default=None)
    languages = models.ManyToManyField(Languages, default=None)
    questions = models.ManyToManyField(Question, default=None)
    instagram = models.ManyToManyField(Instagram, default=None)
    spotify = models.ManyToManyField(Spotify, default=None)
    location = models.ForeignKey(City, default=None, on_delete=models.CASCADE)
    city_of_origin = models.ForeignKey(City, default=None, on_delete=models.CASCADE, related_name="city_origin")
    date_of_birth = models.DateField()
    is_paid_profile = models.BooleanField(default=False)
