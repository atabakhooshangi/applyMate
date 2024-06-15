from django.db import router
from django.urls import path, include
from .views import ApplicationView, ApplicationDetailView, ApplicationUpdateView , ApplicationCreateView

urlpatterns = [
    path('', ApplicationView.as_view(), name='application_list'),
    path('<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('<int:pk>/edit/', ApplicationUpdateView.as_view(), name='application_edit'),
    path('create/', ApplicationCreateView.as_view(), name='application_create'),

]
