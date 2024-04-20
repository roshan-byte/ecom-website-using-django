from django.urls import path 
from . import views 

# conf url 

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail), #int will insure that id should be integer.
    
]