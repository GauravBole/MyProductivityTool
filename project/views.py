from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project


class ProjectApiView(ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all().filter(user=self.request.user)


class ProjectDetailApiView(RetrieveUpdateDestroyAPIView):

    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all().filter(user=self.request.user)

    # owerwrite delete method to set a flag active and deactive projects

    def delete(self, request, *args, **kwargs):

        project_obj = self.get_object()
        project_obj.is_active = False
        project_obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)