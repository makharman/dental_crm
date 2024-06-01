from django.db import models
from doctors.models import Doctors, Assistant, Service, Specialization
from client.models import Client

class Gender(models.Model):
    gender_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.gender_name
    
    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"

class FindOut(models.Model):
    find_out_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.find_out_name
    
    class Meta:
        verbose_name = "Как узнал"
        verbose_name_plural = "Как узнали"
        
class Status(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Ltv(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    specialization_title = models.ForeignKey(Specialization, verbose_name="Специализация", on_delete=models.CASCADE)
    tooth = models.IntegerField("Зубы")
    specialization_cost = models.IntegerField("Цена")
    count = models.IntegerField("Количество")
    total = models.IntegerField("Итого")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "LTV"
        verbose_name_plural = "LTV"

class Client(models.Model):
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    father_name = models.CharField("Отчество", max_length=255)
    gender = models.ForeignKey(Gender, verbose_name="Пол", on_delete=models.CASCADE)
    mobile_phone = models.CharField("Мобильный телефон", max_length=15, null=True, blank=True)
    iin = models.CharField("ИИН", max_length=12, null=True, blank=True)
    date_of_birth = models.DateField("Дата рождения", null=True)
    find_out = models.ForeignKey(FindOut, verbose_name="Как узнал", on_delete=models.CASCADE)
    ltv = models.ForeignKey(Ltv, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

