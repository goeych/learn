from django.urls import path

from . import views

urlpatterns = [
    path('',views.weeklymonitor, name='weeklymonitor'),
    path('listcalibrationrecord',views.ListCalibrationRecord,name='ListCalibrationRecord'),
         ]
