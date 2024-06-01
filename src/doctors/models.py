from django.db import models
from client.models import Client

class Specialization(models.Model):
    title = models.CharField("Название специализации", max_length=255)
    cost = models.IntegerField("Стоимость услуги")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

class Service(models.Model):
    title = models.CharField("Название услуги", max_length=255)
    spec_id = models.ForeignKey(Specialization, verbose_name="Специализация", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Doctors(models.Model):
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    father_name = models.CharField("Отчество", max_length=255)
    body = models.TextField()
    services_id = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

class Assistant(models.Model):
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    father_name = models.CharField("Отчество", max_length=255)
    body = models.TextField()
    services_id = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Ассистент"
        verbose_name_plural = "Ассистенты"

class DoctorClient(models.Model):
    doctor_id = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    
    class Meta:
        verbose_name = "Врач-Клиент"
        verbose_name_plural = "Врачи-Клиенты"
