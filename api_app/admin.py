import imp
from django.contrib import admin
from .models import  *

# Register your models here.
admin.site.register(InterestCategory)
admin.site.register(Interest)
admin.site.register(Languages)
admin.site.register(Question)
admin.site.register(Instagram)
admin.site.register(Spotify)
admin.site.register(Municipio)