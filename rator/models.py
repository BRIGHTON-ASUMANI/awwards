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
        return reverse('profile', kwargs={'pk':self.pk})


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



class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profiler", on_delete=models.CASCADE)
    picture = ImageField()
    contact = models.CharField(max_length =300)
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

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    review = models.CharField(max_length =300)
    created_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.review
