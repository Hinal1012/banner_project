# Generated by Django 2.2.7 on 2019-12-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0007_auto_20191224_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default/default.png', upload_to='profile-pic/'),
        ),
    ]