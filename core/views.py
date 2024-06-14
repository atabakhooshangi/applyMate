from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django_filters.views import FilterView
from core.filters import ApplicationFilter
from core.models import Application, LevelChoices, FeedBackChoices, TypeChoices


class ApplicationView(FilterView, ListView):
    model = Application
    template_name = 'list.html'
    paginate_by = 10
    context_object_name = 'applications'
    filterset_class = ApplicationFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['level_choices'] = LevelChoices.choices
        context['feedback_choices'] = FeedBackChoices.choices
        context['type_choices'] = TypeChoices.choices
        return context


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'detail.html'
    context_object_name = 'application'


class ApplicationUpdateView(UpdateView):
    model = Application
    fields = ['company', 'position', 'level', 'country', 'type', 'source', 'description', 'description_image',
              'company_logo', 'feedback']
    template_name = 'edit.html'
    success_url = reverse_lazy('application_list')
