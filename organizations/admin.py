from django.contrib import admin
from organizations.models import District, Category, Organization, Product, PriceList

admin.site.register(District)
admin.site.register(Category)
admin.site.register(Organization)
admin.site.register(Product)
admin.site.register(PriceList)
