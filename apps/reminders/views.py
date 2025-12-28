from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Reminder
from .forms import ReminderForm


def reminders_list_view(request):
    reminders = Reminder.objects.select_related("task").filter(
        task__completed=False, 
        user=request.user
    ).order_by("reminder_at")

    return render(request, "reminders_list.html", {
        "reminders": reminders
    })


def update_reminder_view(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)

    if request.method == "POST":
        form = ReminderForm(request.POST, instance=reminder)

        if form.is_valid():
            form.save()

            messages.success(request, "Recordatorio actualizado.")
            return redirect("reminders_list")

    else:
        form = ReminderForm(instance=reminder)

    return render(request, "update_reminder_form.html", {
        "form": form,
        "reminder": reminder
    })


def delete_reminder_view(request, reminder_id):
    reminder = get_object_or_404(Reminder, id=reminder_id)
    reminder.delete()

    messages.success(request, "Recordatorio eliminado.")
    return redirect("reminders_list")
