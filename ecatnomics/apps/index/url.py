from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^cat/(?P<pk>[a-zA-Z0-9]+)/?$', views.CustomerView.as_view(), name="customer"),
    url(r'^merchants/(?P<pk>[a-zA-Z0-9]+)/?$', views.MerchantsView.as_view(), name="merchants"),
    url(r'^merchantsIndex', views.MerchantsIndexView.as_view(), name="merchantsIndex"),
]
