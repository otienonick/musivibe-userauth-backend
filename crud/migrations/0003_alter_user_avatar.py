# Generated by Django 3.2.8 on 2021-11-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='profile.jpg', upload_to='uploads/'),
        ),
    ]
