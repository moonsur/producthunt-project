from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='media/')
    icon = models.ImageField(upload_to='media/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d %Y')
