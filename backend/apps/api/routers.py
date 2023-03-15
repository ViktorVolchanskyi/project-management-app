from rest_framework.routers import DefaultRouter
from apps.customer import views as customer_views


router = DefaultRouter()

router.register('customer', customer_views.CustomerViewSet, basename='customer')
