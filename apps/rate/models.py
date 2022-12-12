from django.db import models


class Rate(models.Model):
    session = models.IntegerField()
    price = models.IntegerField()

    # def __str__(self):
    #     return self.session

