from django.db import models


class LevelChoices(models.TextChoices):
    INTERN = 'Intern', 'Intern'
    ENTRY = 'Entry', 'Entry'
    JUNIOR = 'Junior', 'Junior'
    SENIOR = 'Senior', 'Senior'
    LEAD = 'Lead', 'Lead'
    MANAGER = 'Manager', 'Manager'


class TypeChoices(models.TextChoices):
    HYBRID = 'Hybrid', 'Hybrid'
    REMOTE = 'Remote', 'Remote'
    ONSITE = 'Onsite', 'Onsite'


class FeedBackChoices(models.TextChoices):
    NO_FEEDBACK = 'No Feedback', 'No Feedback'
    REJECTED = 'Rejected', 'Rejected'
    INTERVIEW = 'Interview', 'Interview'
    OFFER = 'Offer', 'Offer'


def upload_location(instance, filename):
    extension = filename.split('.')[-1]
    if len(Application.objects.all()) > 0:
        app_id = Application.objects.last().id + 1
    else:
        app_id = 1
    return f'description/{instance.company}-{app_id}-descr.{extension}'


def logo_upload_location(instance, filename):
    extension = filename.split('.')[-1]
    if len(Application.objects.all()) > 0:
        app_id = Application.objects.last().id + 1
    else:
        app_id = 1
    return f'logo/{instance.company}-{app_id}-logo.{extension}'


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Application(BaseModel):
    company = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to=logo_upload_location, blank=True, null=True)
    position = models.CharField(max_length=255)
    level = models.CharField(choices=LevelChoices.choices, max_length=255)
    country = models.CharField(max_length=255)
    type = models.CharField(max_length=255, db_column='type', choices=TypeChoices.choices)
    description = models.TextField()
    description_image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    feedback = models.CharField(choices=FeedBackChoices.choices, max_length=255, default=FeedBackChoices.NO_FEEDBACK)
    source = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ('-created_at',)
