from django.db import models
from django.utils import timezone
from datetime import timedelta
from apps.projects.models import Project  # ajusta el import según tu estructura

class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Proyecto"
    )
    title = models.CharField(
        max_length=150,
        verbose_name="Título de la tarea"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de vencimiento"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="Completada"
    )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ["completed", "due_date"]

    @property
    def is_expired(self):
        return self.due_date and self.due_date < timezone.now().date()

    @property
    def is_near_expiration(self):
        if not self.due_date:
            return False
        return timezone.now().date() <= self.due_date <= (timezone.now().date() + timedelta(days=2))

    def __str__(self):
        return f"{self.title} ({self.project.name})"
