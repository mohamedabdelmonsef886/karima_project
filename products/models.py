from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم المنتج')
    description = models.TextField(verbose_name='الوصف', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    image = models.ImageField(upload_to='products/', verbose_name='صورة المنتج')
    category = models.CharField(max_length=100, default='عبايات', verbose_name='الفئة')  # عبايات، زي إسلامي
    stock = models.IntegerField(default=0, verbose_name='المخزون')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'منتج'
        verbose_name_plural = 'المنتجات'