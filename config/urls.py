from django.contrib import admin
from django.urls import path, include
from apps.projects.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name='home'),
    path("home/", home_view),
    path("users/", include("apps.users.urls")),
    path("projects/", include("apps.projects.urls")),
]

