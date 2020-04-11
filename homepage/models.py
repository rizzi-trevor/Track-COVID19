from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=5)
    date = models.DateField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        report = '@' + str(self.date) + ' ' + self.street + ' ' + self.city + ' ' + self.state + ' ' + self.zipcode
        return report

    