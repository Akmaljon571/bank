from django.db import models


class PetitionModel(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=255, null=True)
    date_of_birth = models.CharField(max_length=200, null=True)
    passport_seriya = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    selectTerm = models.IntegerField(null=True)
    selectSumma = models.IntegerField(null=True)
    reasons = models.CharField(max_length=200, null=True)
    oldCredit = models.IntegerField(null=True)
    residue = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    kafil = models.CharField(max_length=200, null=True)
    delay = models.CharField(max_length=200, null=True)
    user_password = models.CharField(max_length=200, null=True)
    credit_id = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/')
