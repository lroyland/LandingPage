#from django.shortcuts import render
#from django.views.generic import CreateView
"""
from Form.models import newLead

from django.views.generic import ListView, CreateView, UpdateView

from Form.forms import NewLeadForm

class NewLeadUpdateView(UpdateView):
    model = newLead
    form_class = NewLeadForm
    template_name = 'Form/newLead_form.html'
"""

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from Form.models import Lead
from Form.forms import LeadForm


class LeadListView(ListView):
    model = Lead
    context_object_name = 'leads'


class LeadCreateView(CreateView):
    model = Lead
    fields = ('first_name', 'last_name', 'email', 'phone_number')
    success_url = reverse_lazy('lead_list')


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'Form/lead_update_form.html'
    success_url = reverse_lazy('lead_list')
