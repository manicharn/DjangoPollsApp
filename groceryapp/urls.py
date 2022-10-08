from django.urls import path
from .views import GroceryCartViews,RenderingPages,ItemsTodatabaseApi
from . import views

urlpatterns = [
    path("addcart/",GroceryCartViews.as_view()),
    path("addcart/<int:id>",GroceryCartViews.as_view()),
    path("viewpage/",RenderingPages.as_view()),
    path("itemstodatabase/",ItemsTodatabaseApi.as_view(),name='items-to-database'),
]