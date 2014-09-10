from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<list_id>[0-9]+)/update$', views.update, name='update'),
    url(r'^(?P<list_id>[0-9]+)/save$', views.save, name='save'),
]
