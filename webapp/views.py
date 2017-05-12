from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.postgres.search import SearchVector

from webapp.models import Card

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

def keyword_home(request):
	return render(request, "keyword.html", {})

def advanced_home(request):
	return render(request, "advanced.html", {})	

def keyword(request):
	keyword = request.GET.get('keyword')
	results = []
	try:
		first, last = keyword.split()
		QUERY2 = Card.objects.filter(SubjectName__icontains=first).filter(SubjectName__icontains=last)
		print(first, last)
	except:
		QUERY2 = Card.objects.filter(SubjectName__icontains=keyword)
	try:
		first, last = keyword.split(",")
		QUERY = Card.objects.filter(SubjectDescription__icontains=first).filter(SubjectDescription__icontains=last)
		QUERY3 = Card.objects.filter(PhotoDescription__icontains=first).filter(PhotoDescription__icontains=last)
	except:
		QUERY = Card.objects.filter(SubjectDescription__icontains=keyword)
		QUERY3 = Card.objects.filter(PhotoDescription__icontains=keyword)
	QUERY4= Card.objects.filter(Negative__icontains=keyword)
	for q in QUERY:
		results.append(q)
	for q in QUERY2:
		results.append(q)
	for q in QUERY3:
		results.append(q)
	for q in QUERY4:
		results.append(q)
	return render(request, "search.html", {"cards": results})

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
		print(q)
	
	for q in QUERY2:
		results.append(q)
	for q in QUERY3:
		results.append(q)
	for q in QUERY4:
		results.append(q)
	return render(request, "advsearch.html", {"cards": results})
