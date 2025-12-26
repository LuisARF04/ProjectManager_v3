from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Usuario"
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del proyecto"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Descripción"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de vencimiento"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="Completado"
    )
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha completado"
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        return self.due_date and self.due_date < timezone.now()

    @property
    def is_near_expiration(self):
        if not self.due_date:
            return False
        now = timezone.now()
        return now <= self.due_date <= (now + timedelta(days=2))

    def __str__(self):
        return self.name

    def update_completion_status(self):
        tasks = self.tasks.all()
        has_tasks = tasks.exists()
        all_done = has_tasks and not tasks.filter(completed=False).exists()

        if self.completed != all_done:
            self.completed = all_done
            self.completed_at = timezone.now() if all_done else None
            self.save(update_fields=['completed', 'completed_at'])
