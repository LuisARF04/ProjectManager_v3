from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_project_view, name="create_project"),
    path("update/<int:project_id>/", views.update_project_view, name="update_project"),
    path("delete/<int:project_id>/", views.delete_project_view, name="delete_project"),
]
