from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view())
]