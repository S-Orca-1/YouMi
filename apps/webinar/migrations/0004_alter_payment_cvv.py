# Generated by Django 3.2.16 on 2022-12-09 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0003_auto_20221209_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='cvv',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message="CVV number must be entered in the format: '[XXX]. Up to 3 digits allowed.", regex='[0-9]{3}$')]),
        ),
    ]