from django.shortcuts import render



def achat(request):
    return render(request, 'achat/listAchat.html')
