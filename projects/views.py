from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .form import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = Tag.objects.all()
    context = {
        'project' : projectObj,
        'tags' : tags,
    }
    return render(request, 'projects/project-detail.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            form = ProjectForm()
            
    context = {'form':form}
    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            form = ProjectForm()
            
    context = {'form':form}
    return render(request, 'projects/project-form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    
    return render(request, 'projects/delete-template.html',context)
    