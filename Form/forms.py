from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from Form.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('first_name','last_name','email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save lead'))
