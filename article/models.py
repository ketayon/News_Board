from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField(max_length = 200)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default = 0)
    author_name = models.ForeignKey(User,on_delete=models.CASCADE, related_name='article_msgs')
    
    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
