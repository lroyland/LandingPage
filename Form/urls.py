"""
from django.urls import path

from Form.views import LeadListView, LeadCreateView, LeadUpdateView


urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('add/', LeadCreateView.as_view(), name='lead_add'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead_edit'),
]
"""
