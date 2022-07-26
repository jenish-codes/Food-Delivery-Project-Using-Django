from django.urls import path
from .views import home, contact, about, feature, menu, chef, blog, blogDetails, booking


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('feature/', feature, name="feature"),
    path('chef/', chef, name="chef"),
    path('menu/', menu, name="menu"),
    path('booking/', booking, name="booking"),
    path('blog/', blog, name="blog"),
    path('blog-details/', blogDetails, name="blog-details"),
    path('contact-us/', contact, name="contact-us"),
]