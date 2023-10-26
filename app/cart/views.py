from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from home.models import Item
from cart.models import Cart, Cart_Item, Bought_Log
from django.contrib.auth.models import User

def cart(request):
		user = request.user
		if not user.is_authenticated:
			return HttpResponseRedirect(reverse('accounts:login'))
		try:
			cart = Cart.objects.get(cart_id=user)
		except Cart.DoesNotExist:
			cart = Cart.objects.create(cart_id=user)
		items = cart.cart_item_set.all()
		total_price = 0
		for item in items:
			total_price += item.item.price * item.quantity
		return render(request, 'cart.html', {'items': items, 'total_price': total_price})

def add(request, item_id):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:login'))
	if not request.method == 'POST':
		return HttpResponse("Invalid request")
	quantity = int(request.POST['quantity'])
	if quantity <= 0:
		return HttpResponse("Invalid quantity")
	try:
		item = Item.objects.get(id=item_id)
	except Item.DoesNotExist:
		return HttpResponse("Item not found")
	try:
		cart = Cart.objects.get(cart_id=user)
	except Cart.DoesNotExist:
		cart = Cart.objects.create(cart_id=user)
	try:
		cart_item = Cart_Item.objects.get(cart=cart, item=item)
		cart_item.quantity += quantity
		cart_item.save()
	except Cart_Item.DoesNotExist:
		cart_item = Cart_Item.objects.create(cart=cart, item=item, quantity=quantity)
	cart.items.add(item, through_defaults={'quantity': cart_item.quantity})
	cart.save()
	return HttpResponseRedirect(reverse('cart:cart'))

def remove(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:login'))
	if not request.method == 'POST':
		return HttpResponse("Invalid request")
	cart_item_id = request.POST['cart_item_id']
	try:
		cart = Cart.objects.get(cart_id=user)
	except Cart.DoesNotExist:
		cart = Cart.objects.create(cart_id=user)
		return HttpResponse("Cart is empty")
	try:
		Cart_Item.objects.get(id=cart_item_id).delete()
		cart.save()
	except Cart_Item.DoesNotExist:
		return HttpResponse("Item not found")
	cart.save()
	return HttpResponseRedirect(reverse('cart:cart'))

def purchase(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:login'))
	if not request.method == 'POST':
		return HttpResponse("Invalid request")
	try:
		cart = Cart.objects.get(cart_id=user)
	except Cart.DoesNotExist:
		cart = Cart.objects.create(cart_id=user)
		return HttpResponse("Cart is empty")
	items = cart.cart_item_set.all()
	for item in items:
		if item.quantity > item.item.stock:
			return HttpResponse("Item out of stock")
	for item in items:
		Bought_Log.objects.create(user=user, item=item.item, quantity=item.quantity)
		item.item.stock -= item.quantity
		item.item.save()
		item.delete()
	cart.save()
	return HttpResponseRedirect(reverse('home:index'))