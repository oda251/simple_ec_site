from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Item
from cart.models import Bought_Log
from django.contrib.auth.models import User

def index(request):
		items = Item.objects.filter(stock__gte=1)
		return render(request, 'home.html', {'items': items})

def detail(request, item_id):
		try:
			item = Item.objects.get(id=item_id)
			return render(request, 'item_detail.html', {'item': item})
		except Item.DoesNotExist:
			return HttpResponse("Item not found")

def item_post(request):
	if request.method == 'GET':
		return render(request, 'item_post.html')
	elif request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		price = int(request.POST['price'])
		quantity = int(request.POST['quantity'])
		if not name or not price or not quantity:
			return HttpResponse("Invalid input")
		item, created = Item.objects.get_or_create(name=name, defaults={'description': description, 'price': price, 'stock': quantity})
		if created:
			return HttpResponseRedirect(reverse('home:index'))
		else:
			if description:
				item.description = description
			item.price = price
			item.stock += quantity
			item.save()
			return HttpResponseRedirect(reverse('home:item_detail', args=(item.id,)))

def bought_log(request):
	user = request.user
	if not user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:login'))
	if not user.is_superuser:
		return HttpResponse("Permission denied")
	bought_logs = Bought_Log.objects.all()
	return render(request, 'bought_log.html', {'bought_logs': bought_logs})