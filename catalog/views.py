from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'base.html')


def contacts(request):
    return render(request, 'contacts.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
