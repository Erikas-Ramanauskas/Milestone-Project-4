# Generated by Django 4.1 on 2024-01-05 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_quality"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quality",
            field=models.ForeignKey(
                blank=True,
                max_length=254,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.quality",
            ),
        ),
    ]
