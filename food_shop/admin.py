from django.contrib import admin
from food_shop.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'added_on', 'is_approved']

admin.site.site_header = "Food Delivery | Admin Dashboard"
admin.site.register(Contact, ContactAdmin)
