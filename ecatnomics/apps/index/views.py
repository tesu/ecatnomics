from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import requests

class IndexView(generic.TemplateView):
    template_name = 'index/index.html'
