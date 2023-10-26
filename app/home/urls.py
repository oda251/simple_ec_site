from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('bought_log', views.bought_log, name='bought_log'),
	path('post', views.item_post, name='item_post'),
	path('<int:item_id>', views.detail, name='item_detail'),
	path('', views.index, name='index'),
]