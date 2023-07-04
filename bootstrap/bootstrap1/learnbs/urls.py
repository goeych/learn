
from django.urls import path
from . import views

app_name='learnbs'

urlpatterns = [
    path('',views.index),
]
