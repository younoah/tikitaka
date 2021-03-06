from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product, Order
# Create your views here.
def home(request):
    return render(request, 'home.html')

def how(request):
        return render(request, 'how.html')

def introduce(request):
        return render(request, 'introduce.html')

def product(request):
    products = Product.objects
    return render(request, 'product.html', {'products' : products})

def list(request):
    orders = Order.objects.order_by('-id')
    return render(request, 'list.html', {'orders' : orders})

def order(request):
    products = Product.objects
    return render(request, 'order.html', {'products' : products})

def create(request):

    selected_product = ''
    tot_price = 0
    name = ['쿠키세트', '마들렌', '밀크 스콘', '햄치즈 브레드', '우유']
    products = {}  
    price = {}  
    products[name[0]] = request.GET['쿠키세트']
    products[name[1]] = request.GET['마들렌']
    products[name[2]] = request.GET['밀크 스콘']
    products[name[3]] = request.GET['햄치즈 브레드']
    products[name[4]] = request.GET['우유']

    price[name[0]] = 3000
    price[name[1]] = 1000
    price[name[2]] = 2000
    price[name[3]] = 2000
    price[name[4]] = 800

        
    for i in name:
        if int(products[i]) >= 1:
            selected_product += i + ' : ' + products[i] + '개, '
            tot_price += price[i]*int(products[i])


    order = Order()
    order.customer_name = request.GET['customer_name']
    order.customer_phone = request.GET['customer_phone']
    order.location = request.GET['location']
    order.pub_date = timezone.datetime.now()
    order.select_product = selected_product
    order.tot_price = tot_price
    order.condition = '주문접수'
    order.save()
    return redirect('/list/')