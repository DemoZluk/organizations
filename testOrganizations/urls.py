"""testOrganizations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from organizations import views

urlpatterns = [
  path('', views.home),
  path('organizations/<district_id>', views.get_org_list),  # example: /organizations/1
  path('search/products', views.search_product),  # example: /search/products?name=prod1
  path('details/organization/<organization_id>', views.get_org_details),  # example: /details/organization/1
  path('details/product/<product_id>', views.get_product_details),  # example: /details/product/1
  path('admin/', admin.site.urls),
]
