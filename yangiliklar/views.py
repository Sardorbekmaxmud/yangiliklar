from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CategoryModel,NewModel
from .serializer import CategorySerializer,NewSerializer
from .permissions import IsOwnerPermissions

# Create your views here.
# category CRUD-----------------------------------------------------------------
class AllCategoryView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

class AllUserCategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CategoryModel.objects.filter(user=user)

class CreateCategoryView(generics.CreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerPermissions,)

class DetailUpdateDeleteCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerPermissions,)

# news CRUD -----------------------------------------------------------------------
class AllNewsView(generics.ListAPIView):
    queryset = NewModel.objects.all()
    serializer_class = NewSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AllNewsUserView(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return NewModel.objects.filter(user=user)
    serializer_class = NewSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CreateNewView(generics.CreateAPIView):
    queryset = NewModel.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsOwnerPermissions,)

class DetailUpdateDeleteNewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewModel.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsOwnerPermissions,)

# -------------------------------------------------------------------------------------------
class CategoryNameApiView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            category = NewModel.objects.filter(category=kwargs['pk'])
            serializer = NewSerializer(category,many=True)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)