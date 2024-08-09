from django.shortcuts import render




def fournisseur(request):
    return render(request, 'fournis/listFournisseur.html')
