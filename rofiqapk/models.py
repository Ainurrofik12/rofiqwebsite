from django.db import models

# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=255)
    body =models.TextField()

    def _str_(self):
        return "{}".format(self.title)