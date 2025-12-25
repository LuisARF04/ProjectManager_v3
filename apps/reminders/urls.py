from django.urls import path
from . import views

urlpatterns = [
    path("", views.reminders_list_view, name="reminders_list"),
    path("update/<int:reminder_id>/", views.update_reminder_view, name="update_reminder"),
    path("delete/<int:reminder_id>/", views.delete_reminder_view, name="delete_reminder"),
]
