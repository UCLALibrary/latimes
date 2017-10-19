from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.postgres.search import SearchVector
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from webapp.models import Card
from .forms import FacetedCardSearchForm, SearchForm, FacetedCardAdvancedSearchForm

import json

def homepage(request):
    return render(request, "homepage.html", {})
    
def advanced_home(request):
    return render(request, "advanced_homepage.html", {}) 

def keyword_home(request):
    return render(request, "keyword_homepage.html", {}) 

def contact(request):
    return render(request, "contact.html", {}) 

def request(request):
    return render(request, "request.html", {}) 

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
  facet_fields = ['BoxNumber', 'Negative', 'Year', 'Photographer', 'Location']
  template_name = 'search_results.html'
  paginate_by = 25
  context_object_name = 'object_list'
  #queryset = Card.objects.filter(SubjectName='test')

class FacetedAdvancedSearchView(BaseFacetedSearchView):

  form_class = FacetedCardAdvancedSearchForm
  facet_fields = ['Negative', 'SubjectName', 'SubjectDescription', 'Photographer', 'Location']
  template_name = 'adv_search_results.html'
  paginate_by = 25
  context_object_name = 'object_list'
  #queryset = Card.objects.filter(SubjectName='test')
    
class CardList(ListView):
    model = Card
    #ordering = ['Year','Month','Day']
    paginate_by = 100
    template_name = "card_list.html"
    def get_queryset(self):
        sortBy = self.request.GET.get('sortBy')
        if 'q' in self.request.GET and self.request.GET.get('q') != '':
            search_form = SearchForm(self.request.GET)
            if search_form.is_valid():
                sortBy = self.request.GET.get('sortBy')
                cd = search_form.cleaned_data
                if sortBy == 'Date':
                    results = SearchQuerySet().models(Card).filter(content=cd['q'].replace("'", " ")).order_by('Year','Month', 'Day').load_all()
                if sortBy == '-Date':
                    results = SearchQuerySet().models(Card).filter(content=cd['q'].replace("'", " ")).order_by('-Year','-Month', '-Day').load_all()
                if sortBy == None:
                    results = SearchQuerySet().models(Card).filter(content=cd['q'].replace("'", " ")).load_all()
                elif 'Date' not in sortBy:
                    results = SearchQuerySet().models(Card).filter(content=cd['q'].replace("'", " ")).order_by(sortBy).load_all()
                return results
        elif sortBy != None:
            sortBy = self.request.GET.get('sortBy')
            if sortBy == 'Date':
                results = SearchQuerySet().order_by('Year','Month','Day')
            if sortBy == '-Date':
                results = SearchQuerySet().order_by('-Year','-Month','-Day')
            elif 'Date' not in sortBy:
                results = SearchQuerySet().order_by(sortBy)
            return results
        else:
            return SearchQuerySet()

class BoxList(ListView):
    model = Card
    paginate_by = 40
    template_name = 'box.html'
    #queryset = Card.objects.filter(BoxNumber='81')
    def get_queryset(self):
        box = self.request.GET.get('box')
        sortBy = self.request.GET.get('sortBy')
        if 'sortBy' in self.request.GET and  self.request.GET.get('sortBy') != '':
            if sortBy == 'Date':
                results = SearchQuerySet().filter(BoxNumber=box).order_by('Year','Month','Day')
            if sortBy == '-Date':
                results = SearchQuerySet().filter(BoxNumber=box).order_by('-Year','-Month','-Day')
            elif 'Date' not in sortBy:
                results = SearchQuerySet().filter(BoxNumber=box).order_by(sortBy)
            return results
        else:
            return SearchQuerySet().filter(BoxNumber=box)
        
class DateList(ListView):
    model = Card
    paginate_by = 40
    template_name = 'date.html'
    #queryset = Card.objects.filter(BoxNumber='81')
    def get_queryset(self):
        day = self.request.GET.get('day')
        month = self.request.GET.get('month')
        year = self.request.GET.get('year')
        sortBy = self.request.GET.get('sortBy')
        if 'sortBy' in self.request.GET and  self.request.GET.get('sortBy') != '':
            if sortBy == 'Date':
                results = SearchQuerySet().filter(Year=year,Month=month, Day=day).order_by('Year','Month','Day')
            if sortBy == '-Date':
                results = SearchQuerySet().filter(Year=year,Month=month, Day=day).order_by('-Year','-Month','-Day')
            elif 'Date' not in sortBy:
                results = SearchQuerySet().filter(Year=year,Month=month, Day=day).order_by(sortBy)
            return results
        else:
            return SearchQuerySet().filter(Year=year,Month=month, Day=day)
