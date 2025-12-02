from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_project_view, name="create_project"),
]