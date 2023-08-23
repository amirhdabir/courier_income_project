from django.db.models import F
from incomes_handler_app import models
import datetime


class CourierDailyIncomeRepository:

    """Manages courier daily income model by creating or updating the income value"""

    def __init__(self):      
        self.model = models.CourierDailyIncome

    def create(self, date: datetime.date, income: float, courier: models.Courier) -> models.CourierDailyIncome:
        try:
            courier_daily_income = self.model(date=date, courier=courier, income=income)
            courier_daily_income.save()
            return courier_daily_income
        except Exception as e:
            raise
    
    def update_income(self, date: datetime.date, income: float, courier:models.Courier):
        try:
            related_id = self.model.objects.filter(date=date, courier=courier
                                                   ).update(income=F('income') + income)
            if not related_id:
                self.create(date=date, income=income, courier=courier)
        except Exception as e:
            raise


class CourierWeeklyIncomeRepository:

    """Manages courier weekly income model by creating or updating the income value"""

    def __init__(self):      
        self.model = models.CourierWeeklyIncome

    def create(self, date: datetime.date, income: float, courier: models.Courier) -> models.CourierWeeklyIncome:
        try:
            courier_weekly_income = self.model(saturday_date=date, courier=courier, income=income)
            courier_weekly_income.save()
            return courier_weekly_income
        except Exception as e:
            raise
    
    def update_income(self, date: datetime.date, income: float, courier:models.Courier):
        try:
            updates_count = self.model.objects.filter(saturday_date=date, courier=courier
                                                      ).update(income=F('income') + income)
            if not updates_count:
                self.create(date=date, income=income, courier=courier)
        except Exception as e:
            raise
