from django.db import models


class LastUpdated(models.Model):
    name = models.CharField(max_length=20, unique=True)  # deposit, saving 등
    updated_at = models.DateTimeField(auto_now=True)
