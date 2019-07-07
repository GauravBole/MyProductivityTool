from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProjectManager(models.Manager):
    # Rewrite objects.all() method for get active projects only

    def all(self):
        return super(ProjectManager, self).filter(is_active=True)


class Project(models.Model):
    "Project Model"

    title = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    objects = ProjectManager()

    def __str__(self):
        return str(self.id)


