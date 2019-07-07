from django.db import models

from project.models import Project
from htmlapp.models import AuditModel
from util.file_path import file_path


class TaskManager(models.Manager):
    # Owerwrite method of objects.all() for all active and inactive tasks

    def all(self):
        return super(TaskManager, self).filter(is_active=True)


class Task(models.Model):
    """
    Task Model
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    detail = models.CharField(max_length=100, null=False, blank=False)
    deadline = models.DateTimeField(auto_now=False, null=True)
    is_complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = TaskManager()

    def __str__(self):
        return str(self.id)


class Comment(AuditModel):
    """
    Comment Model
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    detail = models.TextField(null=False)
    attached_file = models.FileField(upload_to=file_path, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

