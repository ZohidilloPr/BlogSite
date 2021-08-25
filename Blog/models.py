from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class PostsModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} WAS PUBLISHED BY {self.author}'

    def get_absolute_url(self):
        return reverse("Blog:Article", kwargs={'id': self.id})
