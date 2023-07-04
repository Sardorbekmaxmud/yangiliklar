from django.urls import path
from .views import (AllCategoryApiView,DetailCategoryApiView,CreateCategoryApiView,UpdateCategoryApiView,DeleteCategoryApiView,
                    AllNewsApiView,DetailNewApiView,CreateNewApiView,UpdateNewApiView,DeleteNewApiView,
                    CategoryNameApiView)

urlpatterns = [
    #category------------------------------------------------------------------------
    path('category/',AllCategoryApiView.as_view()),
    path('category/<int:category_id>/',DetailCategoryApiView.as_view()),
    path('category/create/',CreateCategoryApiView.as_view()),
    path('category/update/<int:category_id>/',UpdateCategoryApiView.as_view()),
    path('category/delete/<int:category_id>/',DeleteCategoryApiView.as_view()),
    # news ---------------------------------------------------------------------------
    path('news/',AllNewsApiView.as_view()),
    path('news/<int:new_id>/',DetailNewApiView.as_view()),
    path('news/create/',CreateNewApiView.as_view()),
    path('news/update/<int:new_id>/',UpdateNewApiView.as_view()),
    path('news/delete/<int:new_id>/',DeleteNewApiView.as_view()),
    # category name url---------------------------------------------------------------
    path('category/name/<int:category_id>/',CategoryNameApiView.as_view()),
]