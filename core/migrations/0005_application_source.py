# Generated by Django 5.0.6 on 2024-06-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_application_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
