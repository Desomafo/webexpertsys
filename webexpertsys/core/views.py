from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.db.models import Max

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .models import *
from .forms import DialogForm

# Create your views here.


class IndexListView(ListView):

    template_name = 'core/index.html'
    context_object_name = 'tablets_list'
    
    def get_queryset(self):
        return [[tablet, tablet.get_description()] for tablet in Tablet.objects.all()[:6]] 


class DialogFormView(FormView):

    template_name = 'core/dialog.html'
    form_class = DialogForm
    
    def form_valid(self, form):
        return render()


class TabletListView(ListView):
    
    model = Tablet


class TabletDetailView(DetailView):

    model = Tablet


def dialog(request):
    
    if 'answers' not in request.session.keys() or \
       'reset_session' in request.POST or \
       'http://127.0.0.1:8000/' == request.META['HTTP_REFERER']:
        request.session['current_prop'] = 1
        request.session['answers'] = {} 

    # if this is a POST request we need to process the form data
    if request.method == 'POST' and 'reset_session' not in request.POST:
        request.session['answers'].update({Property.objects.get(number=int(request.session['current_prop'])).tablet_property: request.POST['picked_param']})
        request.session['current_prop'] += 1

    form = DialogForm(request.session)

    filters = request.session['answers']
    tablet_count = Tablet.objects.filter(**filters).count()
    if tablet_count == 1 or \
       'finish' in request.POST :
        return redirect('core:result')

    print(request.session['answers'], request.session['current_prop'])

    return render(request, 'core/dialog.html', {'form': form})


class ResultListView(ListView):
    
    template_name = 'core/result.html'
    context_object_name = 'result_tablets'

    def get_queryset(self):
        filters = self.request.session['answers']
        result_tablets = Tablet.objects.filter(**filters)

        return result_tablets


