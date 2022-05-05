from django.db import models
from datetime import datetime

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'users'
