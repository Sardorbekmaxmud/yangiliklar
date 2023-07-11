from django.urls import path
from .views import (AllCategoryView,
                    AllUserCategoryView,CreateCategoryView,DetailUpdateDeleteCategoryView,
                    AllNewsView,AllNewsUserView,CreateNewView,DetailUpdateDeleteNewView,
                    CategoryNameApiView)

urlpatterns = [
    #category------------------------------------------------------------------------
    path('category/all/',AllCategoryView.as_view()), # bu login bo'lgan barcha uchun category

    path('category/getcategorybyuser/',AllUserCategoryView.as_view()), # user category
    path('category/create/',CreateCategoryView.as_view()),
    path('category/<pk>/',DetailUpdateDeleteCategoryView.as_view()),
    # news ---------------------------------------------------------------------------
    path('news/all',AllNewsView.as_view()), # bu hamma login bo'lganlar uchun

    path('news/getnewsbyuser/',AllNewsUserView.as_view()), # user yangililari
    path('new/create/',CreateNewView.as_view()),
    path('new/<pk>/',DetailUpdateDeleteNewView.as_view()),
    # category name url---------------------------------------------------------------
    path('category/type/<pk>/',CategoryNameApiView.as_view()),
]