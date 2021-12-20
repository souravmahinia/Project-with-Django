
from django.contrib import admin
from django.urls import path
from django.utils.regex_helper import normalize
from home import views

urlpatterns = [
    path("" , views.index, name='home'),
    path("about" , views.about, name='about'),
    path("contact" , views.contact, name='contact'),
    path("review/<int:myid>", views.review, name='review'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('create',views.Signup, name="create"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout', views.checkout,name="Checkout"),
    path('paymentstatus', views.paymentstatus,name="paymentstatus"),
    path("checkout", views.checkout, name="checkout")

]
