from django.db import models
from blog.models import Tag
from django.core.validators import RegexValidator

card_number = RegexValidator(
    regex=r'[0-9]{16}$',
    message="Card number must be entered in the format: '[XXXX] [XXXX] [XXXX] [XXXX]'. Up to 16 digits allowed."
)
validity_period = RegexValidator(
    regex=r'^[0-9]/[0-9]{4}$',
    message="Validity period number must be entered in the format: '[XX]/[XX]. Up to 4 digits allowed."
)
cvv = RegexValidator(
    regex=r'[0-9]{3}$',
    message="CVV number must be entered in the format: '[XXX]. Up to 3 digits allowed."
)


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


class Payment(models.Model):
    card_number = models.IntegerField(validators=[card_number])
    validity_period = models.CharField(max_length=5, validators=[validity_period])
    cvv = models.IntegerField(validators=[cvv])
    card_holder = models.CharField(max_length=250)

    def __str__(self):
        return self.card_holder
