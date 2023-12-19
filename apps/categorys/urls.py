from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductListCreateView.as_view())
]