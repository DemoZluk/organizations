from rest_framework import routers

from organizations import views

router = routers.DefaultRouter()

router.register(r'organizations', views.OrganizationViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'price_list', views.PriceListViewSet)
