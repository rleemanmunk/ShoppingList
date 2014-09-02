from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from GroceryItem.models import Item, Category, Store

class IndexView(generic.ListView):
    template_name = 'GroceryItem/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.order_by('item_name')[:]

class DetailView(generic.DetailView):
    model = Item
    template_name = 'GroceryItem/detail.html'

def new(request):
    return render(request, 'GroceryItem/new.html', {
    });

