from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from home.models import Item

class Cart(models.Model):
		cart_id = models.ForeignKey(User, verbose_name=_("cart_id"), on_delete=models.CASCADE)
		items = models.ManyToManyField(Item, related_name="items", blank=True, through='Cart_Item')
		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

		def __str__(self):
				return self.cart_id

class Cart_Item(models.Model):
		cart = models.ForeignKey(Cart, verbose_name=_("cart"), on_delete=models.CASCADE)
		item = models.ForeignKey(Item, verbose_name=_("item"), on_delete=models.CASCADE)
		quantity = models.IntegerField(verbose_name=_("quantity"), default=0)
		created_at = models.DateTimeField(auto_now_add=True)

		class Meta:
				unique_together = ('cart', 'item')

		def __str__(self):
				return self.item.name

class Bought_Log(models.Model):
		user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
		item = models.ForeignKey(Item, verbose_name=_("item"), on_delete=models.CASCADE)
		quantity = models.IntegerField(verbose_name=_("quantity"), default=0)
		created_at = models.DateTimeField(auto_now_add=True)

		def __str__(self):
				return self.user.username + " bought " + str(self.quantity) + " " + self.item.name + "(s)" + " at " + self.created_at.strftime("%Y-%m-%d %H:%M:%S") + "\n\t" + "total price: $" + str(self.item.price * self.quantity)