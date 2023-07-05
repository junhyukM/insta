# Generated by Django 4.2.3 on 2023-07-05 01:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                related_name="follower", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
