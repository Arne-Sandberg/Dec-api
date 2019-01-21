from django.urls import path,include
from . import views



urlpatterns = [
    #urls for listing all products and stores
    path('stores/', views.StoresList.as_view(), name='list_stores'),
    path('products/', views.ProductList.as_view(), name='list_products'), #list all products in all stores
    path('products/<int:pk>', views.ProductList.as_view(), name='list_products'),
    #path('stores/<int:pk>', views.StoresList.as_view(), name='list_store_products'),
    
    #urls for detailing a store or product
    #path('stores/<int:store_id>',views.detail_store_view, name='detail_store'),
    #path('stores/<int:store_id>/products/<int:product_id>',views.detail_product_view, name='detail_product'),

    #urls for creating store and product
    #path('stores/create', views.create_store_view, name='create_store'),
    #path('stores/<int:store_id>/products/create', views.create_product_view, name='create_product'),

    #urls for updating stores and product 
    #path('stores/<int:store_id>/update', views.update_store_view, name='update_store'),
    #path('stores/<int:store_id>/products/<int:product_id>/update', views.update_product_view, name='update_product'),
]