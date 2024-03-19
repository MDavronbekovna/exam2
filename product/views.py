from django.shortcuts import render, get_object_or_404

from product.models import Product,Category
from django.core.paginator import Paginator



def main(request):
    product = Product.objects.all()
    
    search = request.GET.get('search')

    if search:
        product = product.filter(title__icontains=search)

    paginator = Paginator(product, 3)
    page = int(request.GET.get('page', 1))
    product = paginator.get_page(page)


    return render(request, 'index.html', {'product': product})
# Create your views here.

def detail_pro(request, id):
   
    product = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'product': product})
