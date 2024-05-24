from django.urls import path
from .views import CarList, CarDetail, CarCreate, CategoryDetail, CategoryList, ModelDetail, ModelList


urlpatterns = [
    path('car/list/', CarList.as_view()),
    path('car/detail/<int:pk>/', CarDetail.as_view()),
    path('car/create/', CarCreate.as_view()),

    path('category/detail/<int:pk>/', CategoryDetail.as_view()),
    path('category/list/', CategoryList.as_view()),

    path('model/list/', ModelList.as_view()),
    path('model/detail/<int:pk>/', ModelDetail.as_view()),
]