from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Phone did not come')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(phone, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    full_name = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER)
    birthday = models.DateField(null=True, blank=True)
    citizenship = models.CharField(max_length=250, null=True, blank=True)
    country_city = models.CharField(max_length=350, null=True, blank=True)
    image = models.ImageField(upload_to='users', null=True, blank=True)
    phone = models.CharField(max_length=13, validators=[phone_regex], unique=True)
    email = models.EmailField(null=True, blank=True)
    social_media = models.CharField(max_length=250, null=True, blank=True)
    is_psychologist = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return f'{self.full_name} {self.phone}'


class Session(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'session', limit_choices_to={'is_psychologist': False})
    psychologist = models.ForeignKey(User, models.SET_NULL, 'session_psy', null=True, blank=True,
                                     limit_choices_to={'is_psychologist': True})
    data = models.DateTimeField()


class PsychologistTime(models.Model):
    day = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
