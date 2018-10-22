from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.urlresolvers import reverse

class Project(models.Model):
    user = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    landing_page = ImageField(manual_crop='')
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(max_length=250)
    post_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

    @classmethod
    def all_projects(cls):
        project = cls.objects.order_by('post_date')
        return project


    @classmethod
    def get_image(cls, id):
        project = cls.objects.get(id=id)
        return project


    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__title__icontains=search_term)
        return project



class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profiler", on_delete=models.CASCADE)
    picture = ImageField()
    contact = models.BigIntegerField()
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('dump', kwargs={'pk':self.pk})




    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod
    def delete_profile(self):
        return self.delete()

    def __str__(self):
        return self.user.username

# class Review(models.Model):
#     RATING_CHOICES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#
#     )
#     project=models.ForeignKey(Project,null=True)
#     user = models.ForeignKey(User,null=True)
#     design=models.IntegerField(choices=RATING_CHOICES,null=True)
#     usability=models.IntegerField(choices=RATING_CHOICES,null=True)
#     content=models.IntegerField(choices=RATING_CHOICES,null=True)
#
#
#     @classmethod
#     def get_all(cls):
#         all_objects = Review.objects.all()
#         return all_objects
