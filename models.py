from django.db import models
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
    name = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100)
    quickintro = models.TextField()
    intro = models.TextField()
    image1 = models.ImageField(upload_to='images', null=True)
    body1 = models.TextField(null=True)
    image2 = models.ImageField(upload_to='images', null=True)
    title2 = models.CharField(max_length=100, null=True)
    body2 = models.TextField(null=True)
    conc = models.TextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

class Usercomments(models.Model):
    name = models.CharField(max_length=100)
    date_posted = models.DateField(default=timezone.now)
    comnt = models.TextField()
    relatedarticle = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f"{self.name}"