from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=255, verbose_name="симптом")
    doctor = models.CharField(max_length=50, verbose_name="лечащий врач")
    description = models.CharField(max_length=255, verbose_name="описание симптома")

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя пользователя")
    password = models.CharField(max_length=50, verbose_name="пароль")

class Clinic(models.Model):
    address = models.CharField(max_length=255, verbose_name="адресс клиники")
    contact = models.CharField(max_length=255, verbose_name="почта")

class Story(models.Model):
    dateReceipt = models.DateField(verbose_name="дата поступления")
    dateDischarge = models.DateField(verbose_name="дата выписки")
    status = models.IntegerField(verbose_name="статус пользователя")
