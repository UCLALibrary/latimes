from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.postgres.search import SearchVector
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from webapp.models import Card
from .forms import FacetedCardSearchForm, SearchForm

import json

def homepage(request):
    return render(request, "homepage.html", {})
    
def box_list(request):
    box = request.GET.get('box')
    QUERY = Card.objects.filter(BoxNumber=box)
    return render(request, "box.html", {"box":QUERY})

def date_list(request):
    year = request.GET.get('year')
    day = request.GET.get('day')
    month=request.GET.get('month')
    QUERY = Card.objects.filter(Year=year, Month=month, Day=day)
    return render(request, "date.html", {"date":QUERY})

def advanced_home(request):
    return render(request, "advanced.html", {}) 

def advanced(request):
    keyword = request.GET.get('keyword')
    year = request.GET.get('year')
    boxnumb =request.GET.get('boxnumb')
    results = []
    try:
        first, last = keyword.split()
        QUERY2 = Card.objects.filter(SubjectName__icontains=first).filter(SubjectName__icontains=last, Year__icontains=year, BoxNumber__icontains=boxnumb)
        print(first, last)
    except:
        QUERY2 = Card.objects.filter(SubjectName__icontains=keyword, Year__icontains=year, BoxNumber__icontains=boxnumb)
    try:
        first, last = keyword.split(",")
        QUERY = Card.objects.filter(SubjectDescription__icontains=first).filter(SubjectDescription__icontains=last, Year__icontains=year, BoxNumber__icontains=boxnumb)
        QUERY3 = Card.objects.filter(PhotoDescription__icontains=first).filter(PhotoDescription__icontains=last, Year__icontains=year, BoxNumber__icontains=boxnumb)
    except:
        QUERY = Card.objects.filter(SubjectDescription__icontains=keyword, Year__icontains=year, BoxNumber__icontains=boxnumb)
        QUERY3 = Card.objects.filter(PhotoDescription__icontains=keyword, Year__icontains=year, BoxNumber__icontains=boxnumb)
    QUERY4= Card.objects.filter(Negative__icontains=keyword, Year__icontains=year, BoxNumber__icontains=boxnumb)
    
    for q in QUERY:
        results.append(q)   
    for q in QUERY2:
        results.append(q)
    for q in QUERY3:
        results.append(q)
    for q in QUERY4:
        results.append(q)
    return render(request, "advsearch.html", {"cards": results})
    
def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get(
            'query',
            ''))[
        :5]
    s = []
    for result in sqs:
        d = {"value": result.object.SubjectDescription, "data": result.object.SubjectName, "data2":results.object.PhotoDescription}
        s.append(d)
    output = {'suggestions': s}
    return JsonResponse(output)
    
class FacetedSearchView(BaseFacetedSearchView):

  form_class = FacetedCardSearchForm
  facet_fields = ['BoxNumber', 'Negative', 'Year']
  template_name = 'search_results.html'
  paginate_by = 25
  context_object_name = 'object_list'
  #queryset = Card.objects.filter(SubjectName='test')
  
class CardList(ListView):
    model = Card
    #ordering = ['BoxNumber']
    paginate_by = 100
    def get_context_data(self, **kwargs):
        if 'q' in self.request.GET:
            search_form = SearchForm(self.request.GET)
            if search_form.is_valid():
                cd = search_form.cleaned_data
                results = SearchQuerySet().models(Card).filter(content=cd['q']).load_all()
                print(results.count())
                context = {
                    'results_list': results,
                    'search_form': search_form,
                    'cd': cd,
                    'total_results': results.count()
                }    
        else:
            context = super(CardList, self).get_context_data(**kwargs)
            context['search_form'] = SearchForm()
        #context['form'] = self.get_form()
        return context
        
class BoxList(ListView):
    model = Card
    paginate_by = 40
    template_name = 'box.html'
    #queryset = Card.objects.filter(BoxNumber='81')
    def get_queryset(self):
        box = self.request.GET.get('box')
        queryset = Card.objects.filter(BoxNumber=box)
        return queryset
        
    def get_context_data(self, **kwargs):
        if 'q' in self.request.GET:
            search_form = SearchForm(self.request.GET)
            if search_form.is_valid():
                cd = search_form.cleaned_data
                results = SearchQuerySet().models(Card).filter(content=cd['q']).load_all()
                print(results.count())
                context = {
                    'results_list': results,
                    'search_form': search_form,
                    'cd': cd,
                    'total_results': results.count()
                }    
        else:
            context = super(BoxList, self).get_context_data(**kwargs)
            context['search_form'] = SearchForm()
        #context['form'] = self.get_form()
        return context
        
class DateList(ListView):
    model = Card
    paginate_by = 40
    template_name = 'date.html'
    #queryset = Card.objects.filter(BoxNumber='81')
    def get_queryset(self):
        day = self.request.GET.get('day')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')
        queryset = Card.objects.filter(Year=year, Day=day, Month=month)
        return queryset
        
    def get_context_data(self, **kwargs):
        if 'q' in self.request.GET:
            search_form = SearchForm(self.request.GET)
            if search_form.is_valid():
                cd = search_form.cleaned_data
                results = SearchQuerySet().models(Card).filter(content=cd['q']).load_all()
                print(results.count())
                context = {
                    'results_list': results,
                    'search_form': search_form,
                    'cd': cd,
                    'total_results': results.count()
                }    
        else:
            context = super(DateList, self).get_context_data(**kwargs)
            context['search_form'] = SearchForm()
        #context['form'] = self.get_form()
        return context
  