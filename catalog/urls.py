from django.urls import path
from .views import ProductView

app_name = "catalog"

urlpatterns = [
    path('flowers/', ProductView.as_view()),
    path('flowers/<int:pk>', ProductView.as_view()),

]