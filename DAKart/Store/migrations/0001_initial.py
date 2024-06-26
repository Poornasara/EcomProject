# Generated by Django 5.0.2 on 2024-03-14 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Category", "0003_alter_category_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("Product_Name", models.CharField(max_length=200, unique=True)),
                ("Slug", models.SlugField(max_length=100, unique=True)),
                ("Description", models.TextField(blank=True, max_length=500)),
                ("Price", models.IntegerField()),
                ("Images", models.ImageField(blank=True, upload_to="photos/Products")),
                ("Stock", models.IntegerField()),
                ("Created_date", models.DateField(auto_now_add=True)),
                ("Modified_date", models.DateField(auto_now_add=True)),
                ("Is_available", models.BooleanField(default=True)),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Category.category",
                    ),
                ),
            ],
        ),
    ]
