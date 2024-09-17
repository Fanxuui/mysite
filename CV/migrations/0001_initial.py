# Generated by Django 5.1.1 on 2024-09-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="addition",
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
                ("item", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                ("school", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("degree", models.CharField(max_length=200)),
                ("time", models.CharField(max_length=200)),
                ("gpa", models.CharField(max_length=200)),
                ("course", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Honor",
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
                ("name", models.CharField(max_length=200)),
                ("time", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Information",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Internship",
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("tutor", models.CharField(max_length=200)),
                ("time", models.CharField(max_length=200)),
                ("content", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Research",
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("tutor", models.CharField(max_length=200)),
                ("time", models.CharField(max_length=200)),
                ("content", models.CharField(max_length=200)),
            ],
        ),
    ]
