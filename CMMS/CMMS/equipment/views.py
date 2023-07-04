from django.shortcuts import render
import datetime
from django.db.models import Q

from .models import Equipment,Calibration,Department
from .forms import AddCalibrationRecordForm

def weeklymonitor(request):
    getdate = datetime.date.today()
    currentdate = getdate.strftime('%d %B %y')
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    weeklymonitors = Calibration.objects.filter(Q(equipment__department__department=q),
                                                Q(complete=False),
                                                )

    departments = Department.objects.all() 
    #weeklymonitors = Equipment.objects.all()
    
    context={'weeklymonitors':weeklymonitors,
             'currentdate':currentdate,
             'departments':departments,}

    return render(request,'equipment/list.html',context)

def ListCalibrationRecord(request):
    calibrations = Calibration.objects.all()
    context ={'calibrations':calibrations}
    return render(request,'equipment/ListCalibrationRecord.html',context)

def AddCalibrationrecord(request):
    form = AddCalibrationRecordForm()
    context ={'form':form}
    return render(request,'equipment/AddCalibrationRecordForm.html',context)

