from django.shortcuts import render

def lista(request):
    return render(request, "main/placeholder.html", {"titulo": "Pagos"})
