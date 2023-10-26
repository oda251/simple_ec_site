from django.urls import path
from . import views

urlpatterns = [
	path('<int:item_id>', views.detail, name='item_detail'),
	path('', views.index, name='index')
]