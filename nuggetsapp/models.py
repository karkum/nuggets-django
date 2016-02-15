from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

    @classmethod
    def get_nuggets_by_user(cls, user):
        return Nugget_User.get_nuggets_by_user(cls, user)

    @classmethod
    def create_new_nugget(cls, owner, text, tags, source):
        return cls.objects.create(
                owner=owner,
                text=text,
                tags=tags,
                source=source,
                is_deleted=False)

    @classmethod
    def add_existing_nugget(cls, nugget):
        pass


class Nugget_User(models.Model):
    nugget = models.ForeignKey(Nugget, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_owner = models.BooleanField()
    is_deleted = models.BooleanField()

    @classmethod
    def get_nuggets_by_user(cls, user):
        return cls.objects.filter(user = user)

