from django.shortcuts import render


# Create your views here.
def x1(request):
    return render(request, "home.html")
