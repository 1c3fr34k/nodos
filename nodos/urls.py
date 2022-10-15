"""nodos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from nodos import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", views.index),
    path("notes", views.notes, name="nodos"),
    path("notes/add", views.add_note, name="add-note"),
    path("notes/delete/<int:id>", views.delete_note, name="delete-note"),
    # path("notes/get/<int:id>", views.get_single_note),
    path("notes/get/all", views.get_notes, name="get-notes"),
    path("notes/done/<int:id>", views.done_note),
    path("notes/progress", views.progressbar, name="progressbar"),
]
