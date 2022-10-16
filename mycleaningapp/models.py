from django.db import models
from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text="Введите имя сотрудника",
        verbose_name="Имя сотрудника",
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию сотрудника",
        verbose_name="Фамилия сотрудника",
    )


# Create your models here.


class Home(models.Model):
    address = models.CharField(
        max_length=100, help_text="Введите адрес дома", verbose_name="Адрес дома"
    )
    number_of_floors = models.IntegerField(
        help_text="Введите этажность дома",
        verbose_name="Этажность дома",
    )


class Duty(models.Model):
    status = models.BooleanField(
        help_text="Введите состояние дежурства", verbose_name="Состояние дежурства"
    )
    home_id = models.ForeignKey(
        "Home",
        on_delete=models.CASCADE,
        help_text=" Выберите дом для дежурства",
        verbose_name="Дом для дежурства",
        null=True,
    )
    employee_id = models.ForeignKey(
        "Employee",
        on_delete=models.CASCADE,
        help_text=" Выберите сотрудника для дежурства",
        verbose_name="Сотрудник для дежурства",
        null=True,
    )
    date_of_duty = models.DateField(
        help_text="Введите дату дежурства",
        verbose_name="Дaтa дежурства",
        null=True,
        blank=True,
    )
