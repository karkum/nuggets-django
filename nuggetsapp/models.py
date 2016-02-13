from django.db import models
from django.utils import timezone

class Nugget(models.Model):
    owner = models.ForeignKey('auth.User')
    text = models.CharField(max_length=200)
    source = models.TextField()
    url = models.TextField()
    tags = models.TextField() # store as JSON?
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField()

    def __str__(self):
        return self.text
