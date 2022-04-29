from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model): 
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    text = models.TextField()
    category = models.CharField(max_length=15, default='other')
    published_date = models.DateTimeField(default=timezone.now)
    creater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='books_covers/', blank=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title