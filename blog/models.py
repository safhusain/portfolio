from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    last_date = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=200)

    def shortSummary(self):
        return self.summary[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title