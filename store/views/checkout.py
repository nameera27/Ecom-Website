from django.shortcuts import redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')

        products = Product.get_products_by_id(list(cart.keys()))
        print(name, email, address, phone, customer, cart, products)

        for product in products:
            # print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          name=name,
                          email =email,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        # request.session['customer'] = {}
        # request.session['cart'] = {}
        return redirect('index')