# Generated by Django 4.1.3 on 2022-12-19 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dbproject", "0007_alter_courseorder_created_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="BalanceOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("top_up_value", models.IntegerField(default=0)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "sys_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbproject.sysuser",
                    ),
                ),
            ],
        ),
    ]