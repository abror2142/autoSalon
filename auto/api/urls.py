from django.urls import path
from .views import CarListCreate, CategoryDetail, CategoryListCreate, ModelDetail, ModelListCreate


urlpatterns = [
    path('car/list-create/', CarListCreate.as_view()),

    path('category/detail/<int:pk>/', CategoryDetail.as_view()),
    path('category/list-create/', CategoryListCreate.as_view()),

    path('model/list-create/', ModelListCreate.as_view()),
    path('model/detail/<int:pk>/', ModelDetail.as_view()),
]