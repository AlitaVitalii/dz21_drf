from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.text