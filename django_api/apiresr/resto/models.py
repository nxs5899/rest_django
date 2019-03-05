from django.db import models

# Create your models here.
class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    desciption = models.TextField(blank=True, default=True)
    total = models.DecimalField(max_digits=7, decimal_places=3)
    paid = models.DecimalField(max_digits=7, decimal_places=2)

