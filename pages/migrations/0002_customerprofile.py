# Generated by Django 3.2.7 on 2021-10-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('age', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('contact_no', models.CharField(blank=True, max_length=10)),
                ('email_add', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]