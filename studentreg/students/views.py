from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from django.contrib.admin import User

# Create your views here.
def home(request):
    template= loader.get_template('index.html')
    return HttpResponse(template.render())

'''def students(request):
    mystudents = User.objects.all().values()
    template = loader.get_template('student_reg.html')
    context = {
        'mystudents': mystudents,    
        }
    return HttpResponse(template.render(context,request))'''
