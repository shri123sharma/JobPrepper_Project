from django.contrib import admin
from ecommerce_app.models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email','is_active','date_joined']
admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)


