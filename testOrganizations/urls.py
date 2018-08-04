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
from django.urls import path, include

from organizations import views
from organizations.rest_router import router

urlpatterns = [
  # Home
  path('', views.home),

  path('rest/', include(router.urls)),

  # Organization list. Example: /organizations/
  path('organizations/', views.OrganizationList.as_view()),

  # Organization list by district. Example: /organizations/1
  path('organizations/<int:district_id>', views.OrganizationList.as_view()),

  # Search product by name. Example: /search/products?name=prod1
  path('search/products', views.ProductSearch.as_view()),

  # Product list by organization with filtering. Example: /products?min_price=10&organization=1
  # Filters: organization, min_price, max_price, category
  path('products', views.ProductFilter.as_view()),

  path('admin/', admin.site.urls),
]
