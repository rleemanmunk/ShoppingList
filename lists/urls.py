from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.new, name='new'),
]
