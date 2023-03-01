from django.shortcuts import render
from bpForms.forms import projectForm
from bpForms.models import Project

def index(request):
    return render(request, 'bpForms/index.html')

def listUsers(request):
    userlist = Project.objects.all()
    return render(request, 'bpForms/listUsers.html', {'users':userlist})


def addUser(request):
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'bpForms/addUser.html', {'form': form})


