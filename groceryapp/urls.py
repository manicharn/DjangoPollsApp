from django.urls import path
from .views import GroceryCartViews

urlpatterns = [
    path("addcart/",GroceryCartViews.as_view()),
    path("addcart/<int:id>",GroceryCartViews.as_view()),
]