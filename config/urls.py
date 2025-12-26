from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.projects.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),
    path("home/", home_view),
    path("users/", include("apps.users.urls")),
    path("projects/", include("apps.projects.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path("reminders/", include("apps.reminders.urls")),

    # 1. El usuario pide restablecer contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),

    # 2. Mensaje de "te enviamos un correo"
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),

    # 3. El link que llega al correo (donde el usuario pone la nueva clave)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),

    # 4. Mensaje de "Listo, contraseña cambiada"
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name='password_change_done'),
]
