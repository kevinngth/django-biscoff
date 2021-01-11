from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
	path('new/', views.new_product, name="new_product_form"),
	path('create/', views.create_product, name="create_product"),
	path('', views.list_products, name="list_products"),
	# path('<int:product_id>/', views.get_product, name="get_product"),
	# path('<int:product_id>/edit', views.edit_product, name="edit_product_form"),
	# path('<int:product_id>/update', views.update_product, name="update_product"),
	# path('<int:product_id>/delete', views.delete_product, name="delete_product"),
]
