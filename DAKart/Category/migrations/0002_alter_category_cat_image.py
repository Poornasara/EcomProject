# Generated by Django 5.0.2 on 2024-03-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="Cat_Image",
            field=models.ImageField(
                blank=True, upload_to="photos/Categories", verbose_name="Category Image"
            ),
        ),
    ]
