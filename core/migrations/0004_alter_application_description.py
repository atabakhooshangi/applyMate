# Generated by Django 5.0.6 on 2024-06-14 12:19

from django.db import migrations , models
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_application_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField()
        ),
    ]
