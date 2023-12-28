from django.db import models


class CreditModel(models.Model):
    minTerm = models.IntegerField()
    maxTerm = models.IntegerField()
    minSumma = models.IntegerField()
    maxSumma = models.IntegerField()
    percentage = models.IntegerField()
    types = models.CharField(max_length=255)

    def __str__(self):
        return self.types