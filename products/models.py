from django.db import models


# Create your models here.
class Product(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:

		db_table = 'product'
