from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('allproducts/', views.allproducts, name='allproducts'),
    path('<int:product_id>', views.details, name='product_details'),
    path('upvote/<int:product_id>', views.upvote, name='upvote'),
]
