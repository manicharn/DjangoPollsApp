
from django.urls import path
from .views import ShoppingCart,GetcartData,ShoppingCartUpdate,ShoppingCartDelete

urlpatterns = [
    
    path("addcart/",ShoppingCart.as_view()),
    path("getcart/",GetcartData.as_view()),
    path("updatecart/<int:item_id>",ShoppingCartUpdate.as_view()),
    path("deleteitem/<int:item_id>",ShoppingCartDelete.as_view()),
]