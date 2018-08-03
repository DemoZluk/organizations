from django.db.models import Min, Max
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from organizations.models import Organization, Product


def home(request):
  return render(request, 'home.html')


def get_org_list(request, district_id):
  org_list = Organization.objects.filter(district_id=district_id)
  response = dict(district_id=district_id, organizations=[dict(id=org.id, name=org.name) for org in org_list])

  return JsonResponse(response)


def search_product(request):
  query = request.GET.get('name')
  if query:
    product_list = Product.objects.filter(name__contains=query)
  else:
    product_list = Product.objects.all()

  response = dict(query=query, products=[dict(id=prod.id, name=prod.name) for prod in product_list])

  return JsonResponse(response)


def get_org_details(request, organization_id):
  org = get_object_or_404(Organization, id=organization_id)

  response = dict(id=organization_id, name=org.name, description=org.description)

  return JsonResponse(response)


def get_product_list(request, organization_id):
  params = request.GET
  products = Organization.objects.get(id=organization_id).products
  if params.get('category'):
    products = products.filter(category=params.get('category'))
  if params.get('min_price'):
    products = products.filter(pricelist__price__gte=params.get('min_price'))
  if params.get('max_price'):
    products = products.filter(pricelist__price__lte=params.get('max_price'))

  response = dict(params=params, list=[dict(id=prod.id, name=prod.name, price=prod.pricelist_set.first().price) for prod in products.all()])

  return JsonResponse(response)


def get_product_details(request, product_id):
  product = get_object_or_404(Product, id=product_id)

  response = dict(id=product_id, name=product.name)

  return JsonResponse(response)
