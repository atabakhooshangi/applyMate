# Generated by Django 5.0.6 on 2024-06-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_application_company_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
