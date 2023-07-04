from .models import Equipment,Calibration,Department
from django.forms import ModelForm

class AddCalibrationRecordForm(ModelForm):
    class Meta:
        model = Calibration
        fields = '__all__'
        
