from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer


class TaskApiView(ListCreateAPIView):
    """
    create and list all tasks
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailApiView(RetrieveUpdateDestroyAPIView):
    """
    Retrive update and distroy tasks on perticular pk
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    # owerwrite delete method for active and deactie task

    def delete(self, request, *args, **kwargs):
        task_obj = self.get_object()
        task_obj.is_active = False
        task_obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentApiView(ListCreateAPIView):
    """
    Create and list comments
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

