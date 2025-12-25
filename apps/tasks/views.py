from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from apps.projects.models import Project
from django.utils import timezone
from django.forms import inlineformset_factory
from apps.reminders.models import Reminder
from apps.reminders.forms import ReminderForm

ReminderFormSet = inlineformset_factory(
    Task, Reminder, form=ReminderForm, extra=1, can_delete=False
)

# Crear tarea


def create_task_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = TaskForm(request.POST)
        formset = ReminderFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()

            formset.instance = task
            formset.save()

            messages.success(request, "Tarea creada exitosamente con recordatorio opcional.")
            return redirect("home")

    else:
        form = TaskForm()
        formset = ReminderFormSet()

    return render(request, "task_form.html", {
        "form": form,
        "formset": formset,
        "project": project,
    })



def update_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        formset = ReminderFormSet(request.POST, instance=task)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()

            messages.success(request, "Tarea actualizada correctamente con recordatorio.")
            return redirect("home")

    else:
        form = TaskForm(instance=task)
        formset = ReminderFormSet(instance=task)

    return render(request, "task_form.html", {
        "form": form,
        "formset": formset,
        "project": task.project,
        "task": task,
    })


# Completar tarea


def complete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.completed_at = timezone.now()
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
