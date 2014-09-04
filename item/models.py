from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    verbose_name = "Category"
    verbose_name_plural = "Categories"
    def __str__(self):
        return self.category_name;
    class Meta:
        verbose_name_plural = "categories"

class Store(models.Model):
    store_name = models.CharField(max_length=100) 
    def __str__(self):
        return self.store_name;


class ItemManager(models.Manager):
    def create_item(self, name, cat, price, store):
        book = self.create(item_name = name, category=cat, price=price, store=store)
        return book

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    store = models.ForeignKey(Store)
    objects = ItemManager()
    def __str__(self):
        return self.item_name + "( $" + str(self.price) + " )"

    
