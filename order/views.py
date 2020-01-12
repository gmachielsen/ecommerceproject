from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required()
def orderHistory(request):
    user = request.user
    print(user)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.username)
    if user.is_authenticated:
        email = str(request.user.email)
        order_details = Order.objects.filter(emailAddress=email)
    return render(request, 'order/orderslist.html', {'order_details':order_details})

@login_required()
def viewOrder(request, order_id):
    if request.user.is_authenticated:
        email = str(request.user.email)
        order = Order.objects.get(id=order_id, emailAddress=email)
        order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order/orderdetail.html', {'order':order, 'order_items':order_items})


def thanks(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
        email = str(request.user.email)
    return render(request, 'thanks.html', {'customer_order': customer_order})
