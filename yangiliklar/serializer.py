from rest_framework import serializers
from .models import CategoryModel,NewModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id','name')

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModel
        fields = ('id','category','title','text','create_at','update_at')

