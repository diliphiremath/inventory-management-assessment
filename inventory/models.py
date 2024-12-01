from django.db import models

class Batch(models.Model):
    batch_id = models.CharField(max_length=100)

    def __str__(self):
        return self.batch_id


class Item(models.Model):
    object_id = models.CharField(max_length=100)
    batch = models.ForeignKey(Batch, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.object_id


class Properties(models.Model):
    item = models.ForeignKey(Item, related_name='data', on_delete=models.CASCADE)
    key = models.CharField(max_length=100, blank=False)
    value = models.JSONField(null=True)

    def __str__(self):
        return f"{self.key}: {self.value}"
