from django.db import models
import re
from django.contrib.auth import settings 
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
from mysite.utils import unique_slug_generator
from django.urls import reverse


# Create your models here.



class Content(models.Model):
    title = models.CharField(max_length=200)
    img =  models.ImageField(upload_to='upload/', max_length=100)
    full_text = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    news = 1
    information = 2
    status_choices = (
        (news, 'News'),
        (information, 'Information'),
    )
    status = models.IntegerField(
        choices=status_choices,
        default=news,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    slug = models.SlugField(unique=True, default='', editable=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk, 'slug' : self.slug})

    
    

    @property
    def get_year(self):
        return self.publication_date.year
        
    @property
    def get_month(self):
        return self.publication_date.month

@receiver(pre_save, sender=Content)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)




