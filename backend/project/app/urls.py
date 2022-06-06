from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('api/v1/order', views.order, name='order'),
    path('api/v1/order/<slug:slug>/', views.param, name='param'),
    path('api/v1/order/dates', views.dates, name='dates'),
    path('api/v1/productbought',views.productbought,name='productbought'),
    
    path('retrieveProductsFromApi',views.retrieveProductsFromApi,name='retrieveProductsFromApi')
    # path('accessToApi', views.accessToApi, name='accessToApi'),
]
