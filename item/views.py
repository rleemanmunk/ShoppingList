from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from item.models import Item, Category, Store

class IndexView(generic.ListView):
    template_name = 'item/index.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return {"item_list": Item.objects.all(),
                "store_list": Store.objects.all(),
                "category_list": Category.objects.all()
               }

def detail(request, item_id):
    p = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/detail.html', {
        "item": p,
        "store_list": Store.objects.all(),
        "category_list": Category.objects.all()
    })

def update(request, item_id):
    p = get_object_or_404(Item, pk=item_id)
    p.item_name = request.POST['name']
    p.category = Category.objects.get(pk=request.POST['category'])
    p.price = request.POST['price']
    p.store = Store.objects.get(pk=request.POST['store'])
    p.save()
    return HttpResponseRedirect(reverse('item:detail', args=(p.id,)))

def new(request):
    return render(request, 'item/new.html', {
    })
