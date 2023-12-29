from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main_page"),
    path('search', views.search, name="search"),
    path('projects', views.projects, name="projects_page"),
    path('projects/<project_slug>', views.projectdetails, name="project_detail"),
]
