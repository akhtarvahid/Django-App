from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_data = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    votes_total = models.IntegerField(default=1)

    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %Y')

