from django.db import models


class Pokemon(models.Model):
    title = models.TextField(max_length=200)
