from django.contrib import admin

# Register your models here.
from .models import BookNow, CustomerProfile

class CustomerProfileAdmin(admin.ModelAdmin):
    model = CustomerProfile(admin.ModelAdmin)
    list_display = [ 'full_name','contact_no','address']



admin.site.register(BookNow)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
