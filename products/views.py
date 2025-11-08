from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query)  # بحث
    return render(request, 'products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})  # أضف template لو عايز تفاصيل
from django.shortcuts import render
from .models import Product  # عدل الاسم لو الموديل مختلف

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
      from django.db.models import Q
      results = Product.objects.filter(
          Q(name__icontains=query) | Q(description__icontains=query)
       )
    return render(request, 'search_results.html', {'results': results, 'query': query})
