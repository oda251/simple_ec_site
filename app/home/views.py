from django.http import HttpResponse
from django.shortcuts import render
from .models import Item

def index(request):
		items = Item.objects.all()
		return render(request, 'home.html', {'items': items})

def detail(request, item_id):
		try:
			item = Item.objects.get(id=item_id)
			return render(request, 'item_detail.html', {'item': item})
		except Item.DoesNotExist:
			return HttpResponse("Item not found")