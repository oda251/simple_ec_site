from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('purchase', views.purchase, name='purchase'),
	path('add/<int:item_id>', views.add, name='add'),
	path('remove', views.remove, name='remove'),
	path('', views.cart, name='cart')
]
