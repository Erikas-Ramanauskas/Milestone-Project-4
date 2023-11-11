# Generated by Django 4.1 on 2023-11-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Brands',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='brands',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('9.5', '9.5'), ('10', '10'), ('10.5', '10.5'), ('11', '11'), ('11.5', '11.5'), ('12', '12'), ('12.5', '12.5'), ('13', '13'), ('13.5', '13.5'), ('14', '14'), ('14.5', '14.5')], default='8', max_length=200),
        ),
    ]
