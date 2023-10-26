from django.db import models

class Item(models.Model):
		name = models.CharField(max_length=50, unique=True)
		description = models.CharField(max_length=200, blank=True, default="")
		price = models.IntegerField(blank=False, null=False)
		stock = models.IntegerField(blank=False, null=False)

		def __str__(self):
				return self.name
