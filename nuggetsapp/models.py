from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from datetime import timedelta


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
    def get_nuggets_by_user(cls, user):
        return Nugget_User.get_nuggets_by_user(user)
        
    @classmethod
    def get_todays_review_nuggets_by_user(cls, user):
        return Nugget_User.get_todays_review_nuggets_by_user(user)

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
    def get_nuggets_by_user(cls, user):
        return [x.nugget for x in cls.objects.filter(user = user).filter(is_deleted = False)]
        
    @classmethod
    def get_todays_review_nuggets_by_user(cls, user):
        today = datetime.date.today(); 
        one_day_back = today - timedelta(days=1); 
        three_days_back = today - timedelta(days = 3); 
        one_week_back = today - timedelta(days = 7); 
        two_weeks_back = today - timedelta(days = 14); 
        one_month_back = today - timedelta(days = 30); 
        three_months_back = today - timedelta(days = 3 * 30)
        six_months_back = today - timedelta(days = 6 * 30)
        one_year_back = today - timedelta(days = 12 * 30)
        two_years_back = today - timedelta(days = 24 * 30)
 
        return [x.nugget for x in  cls.objects.filter(Q(user = user) & Q(is_deleted = False) & (Q(created_at__date__gte = one_day_back) | Q(created_at__date__in = [three_days_back, one_week_back, two_weeks_back, one_month_back, three_months_back, six_months_back, one_year_back, two_years_back])))]
     

