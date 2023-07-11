from rest_framework import serializers
from .models import CategoryModel,NewModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewModel
        fields = '__all__'
