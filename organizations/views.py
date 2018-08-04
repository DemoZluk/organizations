from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics

from organizations.models import Organization, Product, PriceList
from organizations.serializers import OrganizationSerializer, ProductSerializer, PriceListSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
  queryset = Organization.objects.all()
  serializer_class = OrganizationSerializer


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class PriceListViewSet(viewsets.ModelViewSet):
  queryset = PriceList.objects.all()
  serializer_class = PriceListSerializer


class OrganizationList(generics.ListAPIView):
  serializer_class = OrganizationSerializer

  def get_queryset(self):
    queryset = Organization.objects.all()

    if self.kwargs and self.kwargs['district_id']:
      queryset = queryset.filter(district=self.kwargs['district_id'])

    return queryset


class ProductSearch(generics.ListAPIView):
  serializer_class = ProductSerializer

  def get_queryset(self):
    queryset = Product.objects.all()
    search_name = self.request.query_params.get('name', None)

    if search_name is not None:
      queryset = queryset.filter(name__contains=search_name)

    return queryset


class ProductFilter(generics.ListAPIView):
  serializer_class = ProductSerializer

  def get_queryset(self):
    queryset = filter_queryset(Product.objects.all(), self.request.query_params)

    return queryset


def filter_queryset(queryset, query_params):
  organization_id = query_params.get('organization', None)
  category = query_params.get('category', None)
  min_price = query_params.get('min_price', None)
  max_price = query_params.get('max_price', None)
  if organization_id is not None:
    queryset = queryset.filter(organization__id=organization_id)
  if category is not None:
    queryset = queryset.filter(category=category)
  if min_price is not None:
    queryset = queryset.filter(price_list__price__gte=min_price)
  if max_price is not None:
    queryset = queryset.filter(price_list__price__lte=max_price)

  return queryset


def home(request):
  return render(request, 'home.html')
