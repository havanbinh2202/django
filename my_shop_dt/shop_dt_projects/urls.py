from django.urls import path
from . import views
from .views import Tai_Khoan_GCBV

urlpatterns = [
    path('',views.home, name='home'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search, name='search'),
    path('category/<str:category_slug>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('settings/taikhoan/', Tai_Khoan_GCBV.as_view(), name='my_account'),
]