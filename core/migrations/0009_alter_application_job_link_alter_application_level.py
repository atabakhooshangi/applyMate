# Generated by Django 5.0.6 on 2024-06-15 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_application_job_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_link',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='level',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Entry', 'Entry'), ('Junior', 'Junior'), ('Associate', 'Associate'), ('Senior', 'Senior'), ('Lead', 'Lead'), ('Manager', 'Manager')], max_length=255),
        ),
    ]
