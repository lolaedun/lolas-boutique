# Generated by Django 3.2 on 2022-04-06 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_icon_socialmedia_socialicon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='socialicon',
            new_name='icons',
        ),
    ]