from django.db import models

# pythonがフォームを自動で生成するためのクラス
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()