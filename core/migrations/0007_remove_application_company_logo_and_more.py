# Generated by Django 5.0.6 on 2024-06-15 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_application_company_logo_uri_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='application',
            name='description_image',
        ),
    ]
