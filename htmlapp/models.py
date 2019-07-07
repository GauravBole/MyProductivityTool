from django.db import models

# Create your models here.


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
