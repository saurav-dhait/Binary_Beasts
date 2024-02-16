from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("user_auth.urls")),
    path("", include("index.urls")),
    path("teacher/", include("teacher.urls")),
    path("student/", include("student.urls")),
]



