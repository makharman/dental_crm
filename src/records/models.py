from django.db import models
from client.models import Client, Ltv
from doctors.models import Doctors, Assistant, Service, Specialization

class RecordsLog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)

class ChairNum(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Номер кабинета"
        verbose_name_plural = "Номера кабинетов"

class RecordingType(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Тип записи"
        verbose_name_plural = "Типы записей"


class PaymentType(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Тип оплаты"
        verbose_name_plural = "Типы оплат"


class PaymentState(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Состояние оплаты"
        verbose_name_plural = "Состояния оплат"

class Record(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True)
    assistant = models.ForeignKey(Assistant, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey(Specialization, verbose_name="Специализация", on_delete=models.CASCADE)
    tooth = models.IntegerField("Зубы")
    specialization_cost = models.IntegerField("Цена") 
    count = models.IntegerField("Количество")
    sell = models.IntegerField("Акции")
    total = models.IntegerField("Итого")
    registration_date = models.DateField("Дата приема")
    record_start = models.DateField("Время начала")
    record_end = models.DateField("Время окончания")
    recording_type = models.ForeignKey(RecordingType, verbose_name="Тип записи", on_delete=models.SET_NULL, null=True)
    notes = models.TextField("Примечания", blank=True)
    reason = models.TextField("Причина", blank=True)
    reception_day = models.DateField()
    chair = models.ForeignKey(ChairNum, verbose_name="Номер кабинета", on_delete=models.SET_NULL, null=True)
    payment_type = models.ForeignKey(PaymentType, verbose_name="Тип оплаты", on_delete=models.SET_NULL, null=True)
    payment_state = models.ForeignKey(PaymentState, verbose_name="Состояние оплаты", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True, null=True)
    
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


