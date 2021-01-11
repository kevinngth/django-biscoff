from django.db import models
#
# from biscoffbakery.products.models import Product
#
#
# # Create your models here.
# class ProductRating(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
# 	rating = models.PositiveSmallIntegerField()
# 	description = models.CharField(max_length=255, blank=True)
# 	created_at = models.DateTimeField(auto_now=True)
# 	updated_at = models.DateTimeField(auto_now=True)
#
# 	class Meta:
# 		db_table = 'product_rating'
