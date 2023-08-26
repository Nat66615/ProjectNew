from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Название'

    )

    manufacture = models.CharField(
        max_length=32,
        verbose_name='Производитель'
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2

    )

    def __str__(self):
        return self.title