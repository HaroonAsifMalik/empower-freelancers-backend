# Generated by Django 5.1.3 on 2025-01-09 11:43

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default=accounts.models.RandomAvatar(), null=True, upload_to='user_images/'),
        ),
    ]