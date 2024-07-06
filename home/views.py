# from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render, redirect
from home.models import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required





# from home.models import Registration,ItemInsert,Contact,Checkout,OrderUpdate,Blogpost
# import json

# from django.db.models import Q



# Create your views here.

def homepage(request):
    context={
        'variable1':"This is sent",
        'variable2':"Aayush"
    }
    return render(request, 'homepage.html', context)


def contact(request):
    thank=False
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        mobile=request.POST.get('mobile', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()
        thank=True
    return render(request, "contact.html", {'thank':thank})


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Already Exsits...")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            username = username,
            last_name = last_name,  
            password = password
        )

        user.set_password(password)
        user.save()
        
        messages.success(request, "Account Created Successfully.")

        return redirect('/login')

    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login')
        
        else:
            login(request, user)
            return redirect('/practice')

    return render(request, 'login.html')

 
def logout_page(request):
    logout(request)
    return redirect('home')
 

def search(request):
    query = request.POST.get('search')
    if len(query)>78:
        item = ItemInsert.objects.none()
    else:
        itemItem_desc= ItemInsert.objects.filter(item_desc__icontains=query)
        itemItem_group= ItemInsert.objects.filter(item_group__icontains=query)
        item= itemItem_desc.union(itemItem_group)
    if item.count() == 0:
        messages.warning(request, "No Search result found. Please refine your query ")    
    params={'item': item, 'query': query}
    return render(request, 'practice.html', params)


def add_to_cart(request):
    print("AAAAA")
    print(request.GET)
    # return HttpResponse('{"status":"added"}')
    if request.method == "GET":

        data = request.GET
        item_insert_id = data.get('item_id')
        user_id = data.get('user_id')
        usr = User.objects.get(id=user_id)

        cart = Cart.objects.filter(user=usr, product=ItemInsert.objects.get(id=item_insert_id))
        if  cart.exists():
            cart = cart.first()
            cart.quantity +=1
            cart.save()
        else:
            Cart.objects.create(user=usr, product=ItemInsert.objects.get(id=item_insert_id), quantity=1)
    return HttpResponse('{"status":"added"}')




#    CART VIEW
def cart(request):
    return render(request, 'homepage.html')


def practice(request):
    item=ItemInsert.objects.all()

    query = request.GET.get('search')
    if query:
        item = ItemInsert.objects.filter(Q(item_group=query) | Q(item_desc=query) )

    print(request.user)
    cart_data =  list(Cart.objects.filter(user=request.user).values("product__item_desc", "product__item_rate", 'quantity'))
    print(cart_data)
    return render(request, 'practice.html',{'item':item, "usr": request.user.id, 'cart_data': cart_data})


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Checkout.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success","updates":updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, "tracker.html")  


def checkout(request):
    if request.method=="POST":
        print(request)
        items_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        addr=request.POST.get('addr', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        number=request.POST.get('number', '')
        checkout = Checkout(items_json=items_json, amount=amount, name=name, email=email, addr=addr, city=city, state=state, zip_code=zip_code, number=number)
        checkout.save()
        update= OrderUpdate(order_id= checkout.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=checkout.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
        
    return render(request, "checkout.html")





def seller(request):
    if request.method=="POST":
        print(request)
        image=request.FILES['image']
        item_desc=request.POST.get('item_desc', '')
        item_group=request.POST.get('item_group', '')
        item_rate=request.POST.get('item_rate', '')
        stock_qty=request.POST.get('stock_qty', '')
        itemInsert = ItemInsert(image=image, item_desc=item_desc, item_group=item_group, item_rate=item_rate, stock_qty=stock_qty, item_date=datetime.today())
        itemInsert.save()
    return render(request, "seller.html") 