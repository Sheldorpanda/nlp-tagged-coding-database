from django.core.paginator import Paginator
from django.shortcuts import render
from display.models import Project
# Create your views here.


def ProjectRender(request):
    project_list = Project.objects.all()
    paginator = Paginator(project_list, 100)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    for project in projects:
        if project.Language == 1:
            project.Language = "Python"
        elif project.Language == 2:
            project.Language = "Java"
        elif project.Language == 3:
            project.Language = "C++"
        elif project.Language == 4:
            project.Language = "Javascript"
        elif project.Language == 5:
            project.Language = "php"
        elif project.Language == 6:
            project.Language = "R"
        elif project.Language == 7:
            project.Language = "Others"
        if project.Level == 1:
            project.Level = "Beginner"
        elif project.Level == 2:
            project.Level = "Intermediate"
        elif project.Level == 3:
            project.Level = "Advanced"
        if project.Popularity == 1:
            project.Popularity = "Inactive for a Long Time"
        elif project.Popularity == 2:
            project.Popularity = "Inactive"
        elif project.Popularity == 3:
            project.Popularity = "Some commits"
        elif project.Popularity == 4:
            project.Popularity = "Active"
        elif project.Popularity == 5:
            project.Popularity = "Very Popular"

    return render(request, 'project_list.html', {'projects': projects})


def search_result(request):
    if request.method == 'GET':
        language = request.GET.get('Language')
        level = request.GET.get('Level')
        popularity = request.GET.get('Popularity')
        legit = request.GET.get('Legit')
        result = Project.objects.all()
        if language:
            result = result.filter(Language=language)
        if level:
            result = result.filter(Level=level)
        if legit:
            result = result.filter(Legit=legit)
        if popularity:
            result = result.filter(Popularity=popularity)
        return render(request, 'project_list.html', {'result': result})
    else:
        return render(request, 'project_list.html', {'result': []})
