from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from apps.projects.models import Project


# Crear tarea


def create_task_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            messages.success(request, "Tarea creada exitosamente.")
            return redirect("home")
    else:
        form = TaskForm()

    return render(request, "task_form.html", {
        "form": form,
        "project": project,
    })


def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Tarea actualizada correctamente.")
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(request, "task_form.html", {
        "form": form,
        "project": task.project,
        "task": task,
    })

# Completar tarea


def complete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()

    messages.success(
        request, f"La tarea '{task.title}' fue marcada como completada.")

    return redirect("home")


# Eliminar tarea


def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Tarea eliminada.")

    return redirect("home")
