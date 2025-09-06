from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/', views.product, name='product'),
]







# from django.urls import path
# from.import views

# urlpatterns = [
#  path('product/',views.product, name='product'),
#  path('',views.products, name='products'),
# ]
    