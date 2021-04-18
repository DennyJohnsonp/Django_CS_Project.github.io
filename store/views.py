from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

print(make_password('1234'))


def index(request):
    return render(request, 'index.html')


def gallery(request):
    return render(request, 'gallery.html')


def cart(request):

    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'cart.html', data)


def validateCustomer(customer):
    error_message = None;
    if (not customer.first_name):
        error_message = "!!! First Name Required !!!"
    elif len(customer.first_name) < 4:
        error_message = "!!! First Name Must Be Greater Than 4 Characters or More !!! "
    elif (not customer.last_name):
        error_message = "!!! Last Name Required !!!"
    elif len(customer.last_name) < 4:
        error_message = "!!! Last Name Must Be Greater Than 4 Characters or More !!! "
    elif (not customer.phone):
        error_message = "!!! Phone Number Required !!!"
    elif len(customer.phone) < 10:
        error_message = "!!! Phone Number Must Be Greater Than 10 Characters or More !!! "
    elif (not customer.password):
        error_message = "!!! Password Required !!!"
    elif len(customer.last_name) < 6:
        error_message = "!!! Password Must Be Greater Than 6 Characters or More !!! "
    elif customer.isExists():
        error_message = "!!!Email Address Already Registered!!!"
    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
    value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
    }
    error_message = None
    customer = Customer(first_name=first_name, last_name=last_name,
                        phone=phone, email=email, password=password)
    error_message = validateCustomer(customer)
    if (not error_message):
        customer.password = make_password(customer.password)
        customer.register()
        return redirect("cart")
    else:
        data ={
            'error': error_message,
            'values': value
        }
    return render(request, 'signup.html',data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
    

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def cart2(request):
    prds = Product.get_all_products()
    return render(request, 'cart2.html',{'products':prds})


def orders(request):
    return render(request, 'orders/orders.html')
