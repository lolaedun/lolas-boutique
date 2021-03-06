# Generated by Django 3.2 on 2022-04-05 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='enter your bio or about us information here')),
                ('facebook', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('github', models.CharField(max_length=100)),
                ('subscribe', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nav_title', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
