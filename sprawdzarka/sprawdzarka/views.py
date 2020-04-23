from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers
from django.shortcuts import render, redirect
from api import models
from .forms import SendedTasksForm
from .models import SendedTasks
class StudentViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.StudentSerializer


def index(request):
    return render(request,"index.html")
#te 2
def task_sended_list(request):
    sended=SendedTasks.objects.all
    return render(request,'task_sended_list.html',{'sended': sended})

def task_sended_upload(request):
    if request.method=='POST':
        form = SendedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=SendedTasksForm()
    return render(request,'task_sended_upload.html', {'form': form})

def read_file(request, file_to_open):
    f = open(r'task/SendedTasks/'+file_to_open, 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

