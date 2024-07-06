from django.contrib import admin
from django.urls import path
from home import views
from home.views import *

from django.conf.urls.static import static




urlpatterns = [
    path("",        views.homepage, name='home'),
    path("contact", views.contact,  name='contact'),
    path('register', views.register_page, name="register"),
    path('login', views.login_page, name="login_page"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),

    # path("stock",   views.stock,    name='stock'),
    path("practice",  views.practice,   name='practice'),
    path("cart",    views.cart,     name='cart'),
    path("tracker", views.tracker,  name='tracker'),
    path("search",  views.search,   name='search'),
    path("checkout",views.checkout, name='checkout'),
    path("seller",views.seller, name='seller'),
    path("add-to-cart",views.add_to_cart, name='add_to_cart'),
    # path("handlerequest",views.handlerequest, name='handlerequest'),
    # path('logout', login_required(logout_user), name='logout'),

]

