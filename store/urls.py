from django.urls import path
from .views import home
from .views.home import Index
from .views.login import Login
from .views.signup import Signup
from .views.cart import CartView
from .views.checkout import CheckOut
from .views.order import OrderView
from django.contrib.auth import views as auth_views
from .middlewares.auth import auth_middleware
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('mens', home.mens,name='mens'),
    path('ladies', home.ladies,name='ladies'),
    path('kids', home.kids,name='kids'),
    path('search/', home.search,name='search'),
    path('about', home.about,name='about'),
    path('contact', home.contact,name='contact'),
    path('services', home.services,name='services'),
    path("products/<int:myid>", home.productView, name="ProductView"),
    path('checkout/',CheckOut.as_view() ,name='checkout'),
    path('cart/',auth_middleware(CartView.as_view()) ,name='cartitem'),
    path('cart/<int:id>',home.deletefromCart ,name='deletefromCart'),
    path('order/', auth_middleware(OrderView.as_view()),name='order'),
    path('signup', Signup.as_view(),name='signup'),
    path('login', Login.as_view(),name='login'),
    path('logout', home.logout,name='logout'),
    
]