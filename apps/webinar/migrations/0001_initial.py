# Generated by Django 3.2.16 on 2022-12-12 12:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Card number must be entered in the format: '[XXXX] [XXXX] [XXXX] [XXXX]'. Up to 16 digits allowed.", regex='[0-9]{16}$')])),
                ('validity_period', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message="Validity period number must be entered in the format: '[XX]/[XX]. Up to 4 digits allowed.", regex='^[0-9]/[0-9]{4}$')])),
                ('cvv', models.IntegerField(validators=[django.core.validators.RegexValidator(message="CVV number must be entered in the format: '[XXX]. Up to 3 digits allowed.", regex='[0-9]{3}$')])),
                ('card_holder', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='webinars')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('price', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('tags', models.ManyToManyField(related_name='webinar', to='blog.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='webinar.webinar')),
            ],
        ),
    ]
