from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Q
from utils import date_for_x_days_before_today

class Nugget(models.Model):
    owner = models.ForeignKey('auth.User')
    text = models.CharField(max_length=200)
    source = models.TextField()
    url = models.TextField()
    tags = models.TextField() # store as JSON?
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    @classmethod
    def get_nuggets_by_user(cls, user, exclude_deleted=True):
        return [x.nugget for x in Nugget_User.get_nugget_users_by_user(user, exclude_deleted)]

    @classmethod
    def get_todays_review_nuggets_by_user(cls, user, exclude_deleted=True):
        return [x.nugget for x in Nugget_User.get_todays_review_nugget_users_by_user(user, exclude_deleted)]

    @classmethod
    def create_new_nugget(cls, user, text, tags, source):
        nugget = cls.objects.create(
                owner = user,
                text = text,
                tags = tags,
                source = source,
                is_deleted = False)
        cls.add_existing_nugget(
                nugget = nugget,
                user = user,
                is_owner = True)
        return nugget

    @classmethod
    def add_existing_nugget(cls, nugget, user, is_owner=False):
        Nugget_User.add_new_nugget_for_user(
                nugget = nugget,
                user = user,
                is_owner = is_owner)


class Nugget_User(models.Model):
    nugget = models.ForeignKey(Nugget, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_owner = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def add_new_nugget_for_user(cls, nugget, user, is_owner=False):
        return cls.objects.create(
                nugget = nugget,
                user = user,
                is_owner = is_owner,
                is_deleted=False)

    @classmethod
    def get_nugget_users_by_user(cls, user, exclude_deleted =True):
        q_objects = Q(user = user)
        if exclude_deleted:
            q_objects.add(Q(is_deleted = False), Q.AND)
        return cls.objects.filter(q_objects)
                
    @classmethod
    def get_todays_review_nugget_users_by_user(cls, user, exclude_deleted =True):
        review_interval_days = [1, 3, 7, 14, 30, 90, 180, 360, 720]
        review_dates = [date_for_x_days_before_today(n) for n in review_interval_days]
        q_objects = Q(user = user) & Q(created_at__date__in = review_dates) #__date casts the datetime value as date
        if exclude_deleted:
            q_objects.add(Q(is_deleted = False), Q.AND)
        return cls.objects.filter(q_objects)

