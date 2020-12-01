from django.contrib.auth.models import User
from django.db import models


class Request(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateField()


class CompositionRequest(models.Model):
    title = models.CharField(max_length=255)
    okpd2 = models.CharField(max_length=100)
    okei = models.CharField(max_length=3)
    quantity = models.PositiveIntegerField()
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


class History(models.Model):
    CREATED = 'CREATED'
    ACCEPTED = 'ACCEPTED'
    FORMED_CALCULATION = 'FORMED_CALCULATION'
    RETURNED = 'RETURNED'
    CONTRACTOR_REMOVED = 'CONTRACTOR_REMOVED'
    EXPIRED = 'EXPIRED'
    STATUS = (
        (CREATED, 'Создан'),
        (ACCEPTED, 'Принят в работу Исполнителем'),
        (FORMED_CALCULATION, 'Сформирован расчет'),
        (RETURNED, 'Возвращен исполнителю'),
        (CONTRACTOR_REMOVED, 'Исполнитель с расчета снят'),
        (EXPIRED, 'Просрочен'),
        )
    status = models.CharField(max_length=100, choices=STATUS, default=CREATED)
    resolution = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


class Calculation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


class PositionCalculation(models.Model):
    composition_request = models.ForeignKey(CompositionRequest, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    calculation = models.ForeignKey(Calculation, on_delete=models.CASCADE)
