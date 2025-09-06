from django.shortcuts import render

from .models import product as ProductModel

def product(request):
    return render(request, 'products/products.html')

def products(request):
    p = ProductModel.objects.all()
    x = {'pro': p.filter(price__in=[10,100,120])}
    return render(request, 'products/products.html', x)






# x = {'pro': p.filter(name__contains='d')}


# x = {'pro': p.filter(name__exact='oppo')}


#  x = {'pro': p.exclude(price =1000)}

# x = {'pro': p.order_by('price')}

#  p = ProductModel.objects.get(price =100)


# from .models import product

# def product(request):
#     return render(request, 'products/product.html')

# def products(request):
#     x={'pro': product.objects.all()}
#     return render(request, 'products/products.html',x)
