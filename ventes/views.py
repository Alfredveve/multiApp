from django.shortcuts import render




def lesVentes(request):
    return render(request, 'vente/listVente.html')
