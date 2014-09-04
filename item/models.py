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

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits = 5, decimal_places=2)
    store = models.ForeignKey(Store)
    def __str__(self):
        return self.item_name + "( $" + str(self.price) + " )"
    
