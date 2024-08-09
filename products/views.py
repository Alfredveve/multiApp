from django.shortcuts import render




def lesProducts(request):
    return render(request, 'product/listProduct.html')
