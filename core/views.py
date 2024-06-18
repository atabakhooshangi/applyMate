import vercel_blob
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django_filters.views import FilterView
from core.filters import ApplicationFilter
from core.models import Application, LevelChoices, FeedBackChoices, TypeChoices
from django.core.paginator import Paginator


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
        context['ordering'] = self.request.GET.get('ordering', 'created_at')

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs
        ordering = self.request.GET.get('ordering', '-updated_at')

        if ordering == 'level':
            queryset = queryset.order_by('level','-created_at')
        elif ordering == '-level':
            queryset = queryset.order_by('-level','-created_at')
        elif ordering == 'created_at':
            queryset = queryset.order_by('created_at','-created_at')
        elif ordering == '-created_at':
            queryset = queryset.order_by('-created_at','-created_at')
        elif ordering == 'updated_at':
            queryset = queryset.order_by('updated_at','-created_at')
        elif ordering == '-updated_at':
            queryset = queryset.order_by('-updated_at','-created_at')
        return queryset


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'detail.html'
    context_object_name = 'application'


class ApplicationUpdateView(UpdateView):
    model = Application
    fields = ['company', 'position', 'level', 'country', 'type', 'source', 'description', 'description_image_uri',
              'company_logo_uri', 'feedback', 'job_link']
    template_name = 'edit.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        obj = self.get_object()
        old_logo_uri = obj.company_logo_uri
        old_descr_uri = obj.description_image_uri
        description_image = self.request.FILES.get('description_image')
        company_logo = self.request.FILES.get('company_logo')
        obj = form.save()
        obj.company_logo_uri = old_logo_uri
        obj.description_image_uri = description_image
        if company_logo is not None:
            logo_file = company_logo.read()
            logo_uri = vercel_blob.put(f"{obj.file_name_prefix}_logo_{obj.id}", logo_file,
                                       {})
            obj.company_logo_uri = logo_uri['url']
            if old_logo_uri is not None:
                vercel_blob.delete(str(old_logo_uri))

        if description_image is not None:
            descr_file = description_image.read()
            descr_uri = vercel_blob.put(f"{obj.file_name_prefix}_descr_{obj.id}", descr_file,
                                        {})

            obj.description_image_uri = descr_uri['url']
            if old_descr_uri is not None:
                vercel_blob.delete(str(old_descr_uri))
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form_invalid-------')
        print(form.errors)
        return super().form_invalid(form)


class ApplicationCreateView(CreateView):
    model = Application
    fields = ['company', 'position', 'level', 'country', 'type', 'source', 'description', 'description_image_uri',
              'company_logo_uri', 'feedback', 'job_link']
    template_name = 'create.html'
    success_url = reverse_lazy('application_list')

    def form_valid(self, form):
        description_image = self.request.FILES.get('description_image')
        company_logo = self.request.FILES.get('company_logo')
        obj = form.save()
        if company_logo is not None:
            logo_file = company_logo.read()
            logo_uri = vercel_blob.put(f"{obj.file_name_prefix}_logo_{obj.id}", logo_file,
                                       {})
            obj.company_logo_uri = logo_uri['url']

        if description_image is not None:
            descr_file = description_image.read()
            descr_uri = vercel_blob.put(f"{obj.file_name_prefix}_descr_{obj.id}", descr_file,
                                        {})

            obj.description_image_uri = descr_uri['url']

        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print('form_invalid-------')
        print(form.errors)
        return super().form_invalid(form)
