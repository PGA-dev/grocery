from django.db import models
from django.utils import timezone

# Create your models here.
class List_items(models.Model):
    groc_item = models.CharField(max_length=70)
    notes = models.TextField()
    item_price = models.DecimalField(max_digits=8, decimal_places=2)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.groc_item

    class Meta:
        verbose_name_plural = "ListItems"