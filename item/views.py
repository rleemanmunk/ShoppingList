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
    # Get user parameters
    item_name = request.POST['name']
    category = Category.objects.get(pk=request.POST['category'])
    price = request.POST['price']
    store = Store.objects.get(pk=request.POST['store'])
    # Check if item was referenced
    try: 
        p = Item.objects.get(pk=item_id)
    except (KeyError, Item.DoesNotExist):
        # If item does not exist, create an item
        p = Item.objects.create_item(item_name, category, price, store)
        return HttpResponseRedirect(reverse('item:index'))
    else:
        # If an item was sent, update that item's attributes
        p.item_name = item_name
        p.category = category
        p.price = price
        p.store = store
        p.save()
        return HttpResponseRedirect(reverse('item:detail', args=(p.id,)))

def new(request):
    return render(request, 'item/new.html', {
        "store_list": Store.objects.all(),
        "category_list": Category.objects.all()
    })
