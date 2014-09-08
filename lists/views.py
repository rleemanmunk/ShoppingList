from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from lists.models import List
from item.models import Item, Category, Store

class IndexView(generic.ListView):
    template_name = 'lists/index.html'
    context_object_name = 'lists'
    def get_queryset(self):
        return List.objects.all()

def new(request):
    return render(request, 'lists/new.html', {
        "item_list": Item.objects.all(),
        "store_list": Store.objects.all(),
        "category_list": Category.objects.all()
    })
