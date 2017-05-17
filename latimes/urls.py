"""latimes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from webapp import views as webapp_views
from webapp.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^box', webapp_views.box_list, name='box_list'),
    url(r'^date', webapp_views.date_list, name='date_list'),
    url(r'^$', webapp_views.homepage, name='homepage'),
    url(r'^keyword', webapp_views.keyword, name='keyword'),
    url(r'^search', webapp_views.keyword_home, name='keyword_home'),
    url(r'^advanced', webapp_views.advanced, name='advanced'),
    url(r'^advsearch', webapp_views.advanced_home, name='advanced_home'),
    url(r'^find', FacetedSearchView.as_view(), name='haystack_search'),

]
