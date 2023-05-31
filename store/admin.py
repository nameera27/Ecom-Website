from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.contact import Contact
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# Register your models here:

admin.site.register(Product,AdminProduct)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Order)
