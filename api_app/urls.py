from django.urls import path
from .views import UserViews

urlpatterns = [
    path('user/', UserViews.as_view())
]