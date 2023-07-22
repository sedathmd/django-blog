from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table='category'
        verbose_name_plural = 'Categories' #admin panelinde sol taraf icin
        verbose_name = 'Category' #admin panelinde ust taraf icin

#admin panelinde her category icin
    def __str__(self): 
        return self.name 