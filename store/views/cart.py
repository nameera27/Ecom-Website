from django.shortcuts import render, redirect,HttpResponse
from django.views import  View
from store.models.product import Product


class CartView(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        # print(products)
        return render(request , 'cart.html' , {'products' : products} )
    

