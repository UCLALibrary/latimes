from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.postgres.search import SearchVector

from webapp.models import Card

import json

def homepage(request):
	return render(request, "homepage.html", {})
	
def card_list(request):
	cards = [str(b.SubjectDescription) for b in Card.objects.all()]
	return HttpResponse(json.dumps(cards))
	
def keyword(request):
	keyword = request.GET.get('keyword')
	year = request.GET.get('year')
	results = []
	QUERY = Card.objects.filter(SubjectDescription__icontains=keyword).filter(Year__icontains=year).values()
	QUERY2 = Card.objects.filter(SubjectName__icontains=keyword).filter(Year__icontains=year).values()
	QUERY3 = Card.objects.filter(PhotoDescription__icontains=keyword).filter(Year__icontains=year).values()
	for q in QUERY:
		results.append(q)
	for q in QUERY2:
		results.append(q)
	for q in QUERY3:
		results.append(q)
	return render(request, "search.html", {"cards": results})
