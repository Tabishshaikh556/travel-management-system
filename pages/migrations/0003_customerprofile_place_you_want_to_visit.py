# Generated by Django 3.2.7 on 2021-10-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_customerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='place_you_want_to_visit',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
