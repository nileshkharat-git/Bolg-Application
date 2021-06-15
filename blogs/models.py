from django.db import models
from accounts.models import Accounts

class Blogs(models.Model):
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Title',null=False)
    article = models.TextField(max_length=1000 ,verbose_name='Article',null=False)
    published_on = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(Accounts,related_name='Likes')

    def total_likes(self):
        return self.likes.count()
