from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact,Orders,Product
from home.models import signup
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from . models import Product
from math import ceil
import json

# Create your views here.


def index(request):

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    #products= Product.objects.all()
    #n= len(products)
    #nSlides= n//4 + ceil((n/4) + (n//4))
    #params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    #allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    #print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request, 'index.html',params)

def about(request):
    return render(request, 'about.html')


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)


    return render(request, 'productview.html', {'product':product[0]})



def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = Contact(email=email, phone=phone, name=name,
                          address=address, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent!!!')

    return render(request, 'contact.html')


def review(request,myid):
    product2 = Product.objects.filter(id=myid)
    return render(request, 'review.html',{'product':product2[0]})

def paymentstatus(request):
    return render(request, 'paymentstatus.html')

def Signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Signup = signup(username=username, email=email, password=password)
        Signup2 = User(username=username, password=password)
        Signup.save()
        Signup2.save()
        messages.success(request, 'Your Account Create Successfuly!!!')

    return render(request, 'create.html')



def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")

def checkout(request):
    #check = Product.objects.filter(id=myid)

    if request.method=="POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        #amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        messages.success(request, 'Address is Saved Successfuly!!!')
        #update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        #update.save()
        #thank = True
        #id = order.order_id
    return render(request, 'checkout.html')
