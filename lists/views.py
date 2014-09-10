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
    return render(request, 'lists/new.html', {})

def create(request):
    p = List.objects.create_list(request.POST['name'])
    p.save()
    return HttpResponseRedirect(reverse('lists:update', args=(p.id,)))

def update(request, list_id):
    l = get_object_or_404(List, pk=list_id)
    return render(request, 'lists/update.html', {
        "list": l, 
        "item_list": Item.objects.all(),
        "store_list": Store.objects.all(),
        "category_list": Category.objects.all()
    })
