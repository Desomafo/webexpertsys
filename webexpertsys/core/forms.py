from django import forms

from .models import *

class DialogForm(forms.Form):

    class Meta:
        fields = ['picked_param']

    def __init__(self, session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        filters = session['answers']
        prop = Property.objects.get(number=int(session['current_prop']))
        choices = Tablet.objects.filter(**filters).values_list(prop.tablet_property, prop.tablet_property)
        print(choices)
        self.fields['picked_param'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, label="Выберете параметр '{}'".format(prop.property_translation))
