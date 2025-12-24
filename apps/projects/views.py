from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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

# Crear proyecto
def create_project_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, "Proyecto creado exitosamente.")
            return redirect("home")

    else:
        form = ProjectForm()

    return render(request, "project_form.html", {"form": form})


# Editar proyecto
def update_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto actualizado correctamente.")
            return redirect("home")

    else:
        form = ProjectForm(instance=project)
        
    return render(request, "project_form.html", {"form": form, "project": project})


# Eliminar proyecto
def delete_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id) 
    
    if request.method == "POST": 
        project.delete() 
        messages.success(request, f"Proyecto '{project.name}' eliminado correctamente.") 
        
    return redirect("home")
