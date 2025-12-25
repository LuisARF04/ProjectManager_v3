from django.db import models
from django.utils import timezone
from apps.tasks.models import Task  # ajusta según tu estructura

class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reminders")
    reminder_at = models.DateTimeField(verbose_name="Fecha y hora del recordatorio")
    notified = models.BooleanField(default=False)

    class Meta:
        ordering = ["reminder_at"]

    def is_due(self):
        return self.reminder_at <= timezone.now() and not self.notified

    def __str__(self):
        return f"Recordatorio de {self.task.title} en {self.reminder_at}"
