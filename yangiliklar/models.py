from django.db import models
from datetime import datetime

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=65,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class NewModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250,default='')
    text = models.TextField(default='')
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'new'
