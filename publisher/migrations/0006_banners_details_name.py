# Generated by Django 2.2.7 on 2019-12-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0005_remove_banners_details_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners_details',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
