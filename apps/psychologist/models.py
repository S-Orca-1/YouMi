from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField


class Education(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'education', limit_choices_to={'is_psychologist': True})
    university = models.CharField(max_length=600)
    faculty = models.CharField(max_length=600)
    specialty = models.CharField(max_length=600)
    degree = models.CharField(max_length=500)
    start = models.DateField()
    finish = models.DateField()
    diplom = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.full_name} {self.university}'


class Specialty(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'specialty', limit_choices_to={'is_psychologist': True})
    job_type = ArrayField(models.CharField(max_length=250))
    academy = models.CharField(max_length=300)
    course = models.CharField(max_length=350)
    training_hours = models.IntegerField()
    start = models.DateField()
    finish = models.DateField()
    certificate = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.full_name} {self.course}'


class ProfessionalData(models.Model):
    ONLINE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    user = models.ForeignKey(User, models.CASCADE, 'pro_data', limit_choices_to={'is_psychologist': True})
    experience_company = models.IntegerField()
    experience_online = models.CharField(max_length=3, choices=ONLINE)
    full_experience = models.IntegerField()
    client = models.IntegerField()
    time = models.IntegerField()
    therapy = models.CharField(max_length=250)
    therapy_hours = models.IntegerField(null=True, blank=True)
    therapy_approach = models.CharField(max_length=350)
    chat = models.CharField(max_length=250)
    chat_hours = models.IntegerField(null=True, blank=True)
    supervisor = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.user.full_name} {self.client}'


class AdditionalQuestion(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'add_ques', limit_choices_to={'is_psychologist': True})
    type = models.CharField(max_length=150)
    salary = models.IntegerField()
    other_job = models.CharField(max_length=50)
    job_time = models.IntegerField()
    about_me = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.full_name} {self.type} {self.salary}'
