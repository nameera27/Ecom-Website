from django.shortcuts import render, redirect
from math import ceil
from store.models.product import Product
from store.models.contact import Contact
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View



class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        return redirect('index')
    
    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # products = None
        allprods = []
        catprod = Product.objects.values('category','id')
        cats = {item['category'] for item in catprod}
        for cat in cats:
            p = Product.objects.filter(category=cat)
            n = len(p)
            nslides = n//4 + ceil((n/4) - (n//4))
            allprods.append([p, range(1, nslides), nslides])
        products = Product.get_all_products()


        params={'allprods':allprods,'products':products}
    
        # print(products)
        return render(request,'index.html',params)


def deletefromCart(request, id):
        cartitem = Product.objects.get(id=id)
        cartitem.delete()
        return render(request,'cart.html')
    

def mens(request):
    mensprod = Product.objects.filter(category_id=1)
    # print(mensprod)
    return render(request,'mens.html',{'mensprod':mensprod})


def ladies(request):
    ladiesprod = Product.objects.filter(category_id=2)
    # print(ladiesprod)
    return render(request,'ladies.html',{'ladiesprod':ladiesprod})


def kids(request):
    kidsprod = Product.objects.filter(category_id=3)
    # print(kidsprod)
    return render(request,'kids.html',{'kidsprod':kidsprod})


def productView(request, myid):
    product=Product.objects.filter(id=myid)
    # print(product)
    return render(request, 'productView.html', {'product':product[0]})


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        phone= request.POST.get('phone','')
        message= request.POST.get('message','')
        # print(name,phone,email,message)
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request,'contact.html')

def logout(request):
    request.session.clear()
    return redirect('index')


def searchMatch(query, item):
    if query in item.name.lower()  or query in item.description.lower():
        return True
    else:
        return False
    

def search(request):
    query= request.GET['query']
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    products = Product.get_all_products()
    params = {'allProds': allProds, 'products':products}
    return render(request, 'search.html', params)