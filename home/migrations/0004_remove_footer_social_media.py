# Generated by Django 3.2 on 2022-04-05 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220405_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='social_media',
        ),
    ]
