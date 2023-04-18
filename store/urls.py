from django.urls import path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
# URLConf
urlpatterns = router.urls + products_router.urls
# urlpatterns = [
#     # path('products/', views.ProductList.as_view()),
#     # path('products/<int:pk>/', views.ProductDetails.as_view()),
#     # path('collection/', views.CollectionList.as_view()),
#     # path('collection/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
# ]