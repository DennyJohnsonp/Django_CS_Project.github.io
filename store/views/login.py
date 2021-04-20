from django.shortcuts import render, redirect
from django.contrib.auth.hashers import  check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Login(View):
    
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                return redirect('cart')
            else:
                error_message = "!!! Invalid User Name or Password!!!"
        else:
            error_message = "!!! Invalid User Name or Password!!!"
        return render(request,'login.html',{'error':error_message})