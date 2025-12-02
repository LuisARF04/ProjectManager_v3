from django.db import models
from django.contrib.auth.models import User

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
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fecha de vencimiento"
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

