from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import *
from .forms import DialogForm

# Create your views here.


class IndexListView(ListView):

    template_name = 'core/index.html'
    context_object_name = 'tablets_list'
    
    def get_queryset(self):
        return [['First tablet', 'First tablet description with some text, some text, some text, some text, some text'], ['Second tablet', 'Second tablet description with some text, some text, some text, some text, some text'], ['Third tablet', 'Third tablet description with some text, some text, some text, some text, some text'], ['Fourth tablet', 'Fourth tablet description with some text, some text, some text, some text, some text'], ['Fiveth tablet', 'Fiveth tablet description with some text, some text, some text, some text, some text'], ['Sixth tablet', 'Sixth tablet description with some text, some text, some text, some text, some text'], ['Seventh tablet', 'Seventh tablet description with some text, some text, some text, some text, some text'], ['Eighth tablet', 'Eighth tablet description with some text, some text, some text, some text, some text']]


class DialogFormView(FormView):

    template_name = 'core/dialog.html'
    form_class = DialogForm
    
