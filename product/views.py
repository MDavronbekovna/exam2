from django.shortcuts import render, get_object_or_404

from product.models import Product, Category
from django.core.paginator import Paginator



def main(request):
    product = Product.objects.all()
    
    search = request.GET.get('search')

    if search:
        product = product.filter(title__icontains=search)

    paginator = Paginator(product, 3)
    page = int(request.GET.get('page', 1))
    product = paginator.get_page(page)
    cats = Category.objects.all()

    context = {
        'product':product,
        'cats':cats,
    }

    return render(request, 'index.html', context)
# Create your views here.

def detail_pro(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'product': product})

def catindex(request, cat_id):
    category1 = Category.objects.get(pk=cat_id)
    cats = Category.objects.all()  # Передаем все категории в контекст
    product = Product.objects.filter(category=category1)
    return render(request, 'catindex.html', {'category1': category1, 'cats': cats, 'product': product})



