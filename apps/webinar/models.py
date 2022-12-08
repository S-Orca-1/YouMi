from django.db import models
from blog.models import Tag


class Webinar(models.Model):
    TYPE = (
        ('Online', 'Online'),
        ('Offline', 'Offline')
    )
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250, choices=TYPE)
    image = models.ImageField(upload_to='webinars', null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, 'webinar')
    price = models.IntegerField(default=0)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    webinar = models.ForeignKey(Webinar, models.CASCADE, 'registration')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.webinar.title}'
