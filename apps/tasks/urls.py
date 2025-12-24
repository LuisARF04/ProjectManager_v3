from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:project_id>/", views.create_task_view, name="create_task"),
    path("update/<int:task_id>/", views.update_task_view, name="update_task"),
    path("complete/<int:task_id>/", views.complete_task_view, name="complete_task"),
    path("delete/<int:task_id>/", views.delete_task_view, name="delete_task"),
]
