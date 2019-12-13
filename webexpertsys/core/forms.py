from django import forms

from .models import *

class DialogForm(forms.Form):

    class Meta:
        fields = ['picked_param']

    def __init__(self, session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        filters = session['answers']
        choises = Tablet.objects.filter(**filters).values_list(Propertie.objects.get(number=session['current_prop'], flat=True))
        self.fields['picked_param'] = forms.ChoiceField(choises)
