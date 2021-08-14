from django.contrib import admin

# Register your models here.
from bestshop.products.models import Product


class BestShopAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', )



admin.site.register(Product, BestShopAdmin)
