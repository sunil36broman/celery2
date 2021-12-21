from django.contrib import admin

# # Register your models here.
# from .models import Distributor,Place,Restaurant,Waiter

# # admin.site.register(Distributor)

# admin.site.register(Place)
# admin.site.register(Restaurant)
# admin.site.register(Waiter)

# class DistributorAdmin(admin.ModelAdmin):
    
#     list_display = [field.attname for field in Distributor._meta.fields]
#     # list_filter = [
#     #      "username",
#     #      "role_name"
#     # ]
#     # search_fields = (
#     #     "username",
#     #     "role_name",
#     # )
#     def has_add_permission(self, request):
#         return False
#     def has_delete_permission(self, request, obj=None):
#         return False   
#     def has_change_permission(self, request, obj=None):
#         return False     

# admin.site.register(Distributor, DistributorAdmin)