from django.shortcuts import render,redirect
from django.views import View
from food_shop.models import Contact


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


# class ContactUS(View):
#     def get(self, request):
#         return render(request, "food_shop/contact.html")

#     def post(self, request):
#         context = {}
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         data = Contact(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#         data.save()
#         context['success_message'] = f"Dear {name}, We will back to you ASAP!"
#         return redirect("contact-us")

def contact_us(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        context['success_message'] = f"Dear {name}, We will back to you ASAP!"
    return render(request, "food_shop/contact.html", context)