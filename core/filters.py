import django_filters
from .models import Application, LevelChoices, FeedBackChoices, TypeChoices


class ApplicationFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(lookup_expr='icontains')
    position = django_filters.CharFilter(lookup_expr='icontains')
    level = django_filters.ChoiceFilter(choices=LevelChoices.choices)
    country = django_filters.CharFilter(lookup_expr='icontains')
    source = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.ChoiceFilter(field_name='type', choices=TypeChoices.choices)
    feedback = django_filters.ChoiceFilter(choices=FeedBackChoices.choices)

    class Meta:
        model = Application
        fields = ['company', 'position', 'level', 'country', 'type', 'feedback','source']
