# Generated by Django 3.2.6 on 2021-09-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, default='profile-default.jpg', upload_to='', verbose_name='Profile-Pic'),
        ),
    ]