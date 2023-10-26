from home.models import Item
from django.http import HttpResponse

def post(request):
	if request.method = 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		price = request.POST.get('price')
		stock = request.POST.get('stock')
		if not name or not price or not stock:
			return HttpResponse("Missing required fields")
		item, created = Item.objects.get_or_create(name=name, defaults={'description': description, 'price': price, 'stock': stock})
		if created:
			return HttpResponse("Item added")
		else:
			if description:
				item.description = description
			item.price = price
			item.stock += stock
			item.save()
			return HttpResponse("Item updated")
