# Generated by Django 5.1 on 2024-08-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utilisateur", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("pseudo", models.CharField(max_length=30, unique=True)),
                ("password", models.CharField(max_length=15)),
                ("creat_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Utilisateur",
        ),
    ]
