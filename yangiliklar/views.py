from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CategoryModel,NewModel
from .serializer import CategorySerializer,NewSerializer

# Create your views here.

# category CRUD-----------------------------------------------------------------
class AllCategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        all_category = CategoryModel.objects.all()
        serializer = CategorySerializer(all_category,many=True)
        return Response(serializer.data)

class DetailCategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        category = get_object_or_404(CategoryModel,pk=kwargs['category_id'])
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CreateCategoryApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateCategoryApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(CategoryModel,pk=kwargs['category_id'])
        serializer = CategorySerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoryApiView(APIView):
    def delete(self,request,*args,**kwargs):
        category = get_object_or_404(CategoryModel,pk=kwargs['category_id'])
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# news CRUD -----------------------------------------------------------------------
class AllNewsApiView(APIView):
    def get(self,request,*args,**kwargs):
        all_news = NewModel.objects.all()
        serializer = NewSerializer(all_news,many=True)
        return Response(serializer.data)

class DetailNewApiView(APIView):
    def get(self,request,*args,**kwargs):
        new = get_object_or_404(NewModel,pk=kwargs['new_id'])
        serializer = NewSerializer(new)
        return Response(serializer.data)

class CreateNewApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateNewApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(CategoryModel,pk=kwargs['new_id'])
        serializer = NewSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteNewApiView(APIView):
    def delete(self,request,*args,**kwargs):
        new = get_object_or_404(NewModel,pk=kwargs['new_id'])
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)