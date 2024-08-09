from django.shortcuts import render




def client(request):
    return render(request, 'clients/listClient.html')
