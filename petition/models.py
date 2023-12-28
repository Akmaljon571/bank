from django.db import models


class PetitionModel(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=200)
    passport_seriya = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    selectTerm = models.IntegerField()
    selectSumma = models.IntegerField()
    reasons = models.CharField(max_length=200)
    oldCredit = models.IntegerField()
    residue = models.IntegerField()
    salary = models.IntegerField()
    kafil = models.CharField(max_length=200)
    delay = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    credit_id = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')