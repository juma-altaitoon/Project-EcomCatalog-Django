# Generated by Django 4.1.4 on 2023-01-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='main_app/static/product-images/'),
        ),
    ]
