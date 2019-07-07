from django.urls import path

from .views import ProjectApiView, ProjectDetailApiView
app_name = "project"

urlpatterns = [
    path('project/', ProjectApiView.as_view(), name="projects"),
    path('project/<int:pk>', ProjectDetailApiView.as_view(), name="projects_detail"),

]