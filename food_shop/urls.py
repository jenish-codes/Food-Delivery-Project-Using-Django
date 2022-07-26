from django.urls import path
from .views import home, about, feature, menu, chef, blog, blogDetails, booking, contact_us


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('feature/', feature, name="feature"),
    path('chef/', chef, name="chef"),
    path('menu/', menu, name="menu"),
    path('booking/', booking, name="booking"),
    path('blog/', blog, name="blog"),
    path('blog-details/', blogDetails, name="blog-details"),
    # path('contact-us/', ContactUS.as_view(), name="contact-us"),
    path('contact-us/', contact_us, name="contact-us"),
]