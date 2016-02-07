from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import requests

class IndexView(generic.TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/customers?key=813882c1bc1595ded762f6bb22bd9ee0')
        context['api'] = r.json()
        for cat in context['api']:
            cat['id'] = cat['_id']
        return context

class CustomerView(generic.TemplateView):
    template_name = 'index/customer.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/customers/' + self.kwargs['pk'] + '?key=813882c1bc1595ded762f6bb22bd9ee0')
        context['api'] = r.json()
        return context

class MerchantsIndexView(generic.TemplateView):
    template_name = 'index/merchantsIndex.html'

    def get_context_data(self, **kwargs):
        context = super(MerchantsIndexView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/merchants?key=813882c1bc1595ded762f6bb22bd9ee0')
        context['api'] = r.json()
        for merchant in context['api']:
            merchant['id'] = merchant['_id']
        context=context[0:10]
        return context

class MerchantsView(generic.TemplateView):
    template_name = 'index/merchants.html'

    def get_context_data(self, **kwargs):
        context = super(MerchantsView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/merchants/' + self.kwargs['pk'] + '?key=813882c1bc1595ded762f6bb22bd9ee0')
        context['api'] = r.json()
        return context
