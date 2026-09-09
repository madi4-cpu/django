from django.core.exceptions import ValidationError
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.title or not self.title.strip():
            raise ValidationError({'title': 'Название обязательно'})

    def __str__(self):
        return self.title