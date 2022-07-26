from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "food_shop/index.html")

def about(request):
    return render(request, "food_shop/about.html")

def feature(request):
    return render(request, "food_shop/feature.html")

def chef(request):
    return render(request, "food_shop/team.html")

def menu(request):
    return render(request, "food_shop/menu.html")

def booking(request):
    return render(request, "food_shop/booking.html")

def blog(request):
    return render(request, "food_shop/blog.html")

def blogDetails(request):
    return render(request, "food_shop/single.html")

def contact(request):
    return render(request, "food_shop/contact.html")