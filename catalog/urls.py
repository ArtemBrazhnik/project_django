from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
    path('catalog/', product_list, name='product_list'),
]
