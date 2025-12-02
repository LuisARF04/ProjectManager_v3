from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home_view(request):
    user = request.user
    projects = Project.objects.filter(user=user)
    return render(request, "home.html", {
        "user" : user,
        "projects": projects,
    })


def create_project_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')

    else:
        form = ProjectForm()

    return render(request, "projects/create_project.html", {"form": form})
