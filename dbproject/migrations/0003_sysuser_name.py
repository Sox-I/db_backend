# Generated by Django 4.1.3 on 2022-12-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dbproject",
            "0002_sysuser_age_sysuser_card_left_time_sysuser_card_time_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="sysuser",
            name="name",
            field=models.CharField(default="", max_length=20),
        ),
    ]
