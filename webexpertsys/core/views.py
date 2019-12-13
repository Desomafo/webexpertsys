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
    
    def form_valid(self, form):
        return render()


def dialog(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # check whether it's valid:
        if len(request.session) == 0:
            request.session['current_prop'] = 1
            request.session['answers'] = {} 
            form = DialogForm({'prop_number': 1})
        else:
            # create a form instance and populate it with data from the request:
            form = DialogForm(request.POST)

        if form.is_valid():
            request.session['answers'].update(request.POST)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
