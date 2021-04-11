from django.shortcuts import render
from django.http import HttpResponse  
from .models.product import Product
from .models.category import Category
from .models.customer import Customer 

def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def cart(request):

    categories = Category.get_all_categories();
    categoryID = request.GET.get('category')
    if categoryID:
        products= Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data={}
    data ['products'] = products
    data['categories'] = categories
    return render(request,'cart.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        customer.register()
        return HttpResponse ("Signup Success")

def cart2(request):
    prds = Product.get_all_products();
    return render(request,'cart2.html',{'products':prds})

def orders(request):
    return render(request,'orders/orders.html')
