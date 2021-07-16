from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    last_date = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=200)
