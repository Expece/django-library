from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model): 
    author = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=50, null=False)
    text = models.TextField(null=False)
    category = models.CharField(max_length=15, null=False)
    published_date = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(upload_to='books_covers/', blank=True, null=True)
    
    def publish(self):
        self.save()
    
    def get_author_and_title(self) -> str:
        return str(self.author), str(self.title)

    def __str__(self):
        return self.title