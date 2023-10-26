from django.db import models

class Client(models.Model):
		name = models.CharField(max_length=50)
		email = models.CharField(max_length=200, blank=True, unique=True, default="example@email.com")
		bougt_items = models.JSONField(default=list, blank=True)
		created_at = models.DateTimeField(auto_now_add=True)

		def __str__(self):
				return self.name