from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import os, random
import requests
import random

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def back(request, page, **kwargs):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse(page, kwargs=kwargs)))

def customer_info(id):
    r = requests.get('http://api.reimaginebanking.com/customers/' + id + '?key=813882c1bc1595ded762f6bb22bd9ee0')
    customer = r.json()
    customer['id'] = customer['_id']
    r = requests.get('http://api.reimaginebanking.com/customers/' + id + '/accounts?key=813882c1bc1595ded762f6bb22bd9ee0')
    customer['accounts'] = r.json()
    o = 0
    for account in customer['accounts']:
        o += account['balance']
    customer['worth'] = o

    random.seed(customer['first_name'] + customer['last_name'])
    customer['image'] = 'cats/' + random.choice(os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)),'../../static/cats/')))

    return customer

# def idk_lol(request, id):
#     requests.post('http://api.reimaginebanking.com/customers/' + id + '/accounts?key=813882c1bc1595ded762f6bb22bd9ee0)')
#     return back(request, 'index:index')

class IndexView(generic.TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/customers?key=813882c1bc1595ded762f6bb22bd9ee0')
        api = r.json()
        context['api'] = []

        for cat in api:
            context['api'].append(customer_info(cat['_id']))
        return context

class FAQView(generic.TemplateView):
    template_name = 'index/faq.html'

class CustomerView(generic.TemplateView):
    template_name = 'index/customer.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        context['api'] = customer_info(self.kwargs['pk'])
        return context

class MerchantsIndexView(generic.TemplateView):
    template_name = 'index/merchantsIndex.html'

    def get_context_data(self, **kwargs):
        context = super(MerchantsIndexView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/merchants?key=813882c1bc1595ded762f6bb22bd9ee0')
        temp = r.json()
        context['api'] = []
        for i in range(10):
        	context['api'].append(temp[random.randint(0,len(temp))])
        '''
        context['api'] = r.json()
        for merchant in context['api']:
            merchant['id'] = merchant['_id']
        context['api']=context['api'][0:10]
       	'''
        return context

class MerchantsView(generic.TemplateView):
    template_name = 'index/merchants.html'

    def get_context_data(self, **kwargs):
        context = super(MerchantsView, self).get_context_data(**kwargs)
        r = requests.get('http://api.reimaginebanking.com/merchants/' + self.kwargs['pk'] + '?key=813882c1bc1595ded762f6bb22bd9ee0')
        context['merchant'] = r.json()
        r = requests.get('http://api.reimaginebanking.com/customers?key=813882c1bc1595ded762f6bb22bd9ee0')
        api = r.json()
        context['api'] = []

        for cat in api:
            context['api'].append(customer_info(cat['_id']))
        return context
