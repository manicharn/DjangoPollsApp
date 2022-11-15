from django.urls import path
from .views import Movetoerror
urlpatterns = [
    path('movetoerror/',Movetoerror.as_view()),
]