# Generated by Django 4.1 on 2024-01-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_rename_productimage_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="banner",
        ),
        migrations.AddField(
            model_name="product",
            name="sold",
            field=models.BooleanField(default=False),
        ),
    ]
