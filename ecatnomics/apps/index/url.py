from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^faq$', views.FAQView.as_view(), name="faq"),
    url(r'^cat/(?P<pk>[a-zA-Z0-9]+)/?$', views.CustomerView.as_view(), name="customer"),
    url(r'^merchants/?$', views.MerchantsIndexView.as_view(), name="merchantsIndex"),
    url(r'^merchant/(?P<pk>[a-zA-Z0-9]+)/?$', views.MerchantsView.as_view(), name="merchants"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
