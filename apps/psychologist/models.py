from django.db import models


class Education(models.Model):
    university = models.CharField(max_length=600)
    faculty = models.CharField(max_length=600)
    specialty = models.CharField(max_length=600)
    degree = models.CharField(max_length=500)
    start = models.DateField()
    finish = models.DateField()
    diplom = models.FileField()

    def __str__(self):
        return self.university
