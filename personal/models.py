from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Addpersonalinfo(models.Model):
    Label = models.CharField(max_length=50)
    Content = models.CharField(max_length=50)
    CreationDate = models.DateTimeField('date published')
    
    def __str__(self):
        return self.Label
        return self.Content
    def was_published_recently(self):
        return self.CreationDate >= timezone.now()
    
#class Choice(models.Model):
#    Label = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)