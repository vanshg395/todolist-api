from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class TasksModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_heading = models.CharField(max_length=100)
    task_description = models.TextField()
    status = models.BooleanField(default=False)
