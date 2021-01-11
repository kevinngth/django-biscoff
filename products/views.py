from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse

from .models import Product


# Create your views here.
def new_product(request):
	return render(request, 'products/new.html')


def create_product(request):
	if request.method != 'POST':
		return HttpResponseNotAllowed(request)

	product = Product.objects.create(
		title=request.POST['title'],
		description=request.POST['description']
	)
	product.save()
	return HttpResponseRedirect(reverse('products:new_product_form'))


def list_products(request):
	products = Product.objects.all()
	return render(request, 'products/index.html', {'products': products})

# def get_product(request):
# 	product = Product.objects.get()
# 	return render(request, 'products/index.html', {'products': products})
