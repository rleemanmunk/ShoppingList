from django.conf.urls import url

from item import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>[0-9]+)/update$', views.update, name='update'),
    url(r'^new/', views.new, name='new'),
]
