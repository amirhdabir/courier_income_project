from django.db import models
from django.db import transaction
from django.core.validators import MinValueValidator
from django.utils import timezone


class Courier(models.Model):

    """Couriers model"""

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class CustomerType(models.Model):

    """Customers type model"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CourierTravel(models.Model):

    """Couriers travel model"""

    origin_distance = models.FloatField(validators=[MinValueValidator(0)])
    travel_distance = models.FloatField(validators=[MinValueValidator(0)])
    customer_type = models.ForeignKey("CustomerType", on_delete=models.PROTECT, db_index=True)
    travel_date_time = models.DateTimeField(default=timezone.now ,db_index=True)
    income = models.FloatField(validators=[MinValueValidator(0)])
    courier = models.ForeignKey("Courier", on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return f'id: {self.id}, courier: {self.courier}'


class CourierTransactionReason(models.Model):

    """The reason for the courier transaction model"""

    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.reason


class CourierTransaction(models.Model):

    """Courier positive or negative transaction model"""

    amount = models.FloatField()
    reason = models.ForeignKey("CourierTransactionReason", on_delete=models.PROTECT)
    courier = models.ForeignKey("Courier", on_delete=models.PROTECT, db_index=True)
    date = models.DateField(default=timezone.now, db_index=True)
    explanation = models.CharField(default='', max_length=500)

    def __str__(self):
        return f'{self.id}'


class CourierDailyIncome(models.Model):

    """Aggregation of all courier income transactions in a day model"""

    date = models.DateField(default=timezone.now, db_index=True)
    income = models.FloatField()
    courier = models.ForeignKey("Courier", on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return f'courier: {self.courier}, date: {self.date}'


class CourierWeeklyIncome(models.Model):

    """Aggregation of all courier income transactions in a week model"""

    saturday_date = models.DateField(db_index=True)
    income = models.FloatField()
    courier = models.ForeignKey("Courier", on_delete=models.PROTECT, db_index=True)

    def __str__(self):
        return f'courier: {self.courier}, saturday_date: {self.saturday_date}'