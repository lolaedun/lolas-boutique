# Generated by Django 3.2 on 2022-04-02 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
