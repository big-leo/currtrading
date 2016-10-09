from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^currencies/$', views.currencies, name='currencies'),
    url(r'^currency/(?P<curr>[A-Z]{3})/$', views.currency, name='currency'),
    url(r'^currency/(?P<curr>[A-Z]{3})/(?P<to>[A-Z]{3})/$', views.currency, name='currency'),
    url(r'^sequence/$', views.sequence, name='sequence'),
    url(r'^$', views.index, name='index'),
]