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
  # Home
  path('', views.home),

  # Organization list by district. Example: /organizations/1
  path('organizations/<district_id>', views.get_org_list),

  # Search product by name. Example: /search/products?name=prod1
  path('search/products', views.search_product),

  # View organization details. Example: /organization/1
  path('organization/<organization_id>', views.get_org_details),

  # Product list by organization with filtering. Example: /organization/1/products?min_price=10
  path('organization/<organization_id>/products', views.get_product_list),

  # View product details. Example: /product/1
  path('product/<product_id>', views.get_product_details),

  path('admin/', admin.site.urls),
]
