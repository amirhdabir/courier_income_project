from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from datetime import date
from incomes_handler_app import models
from incomes_handler_app import models_repositories
from incomes_handler_app import utils


@receiver(post_save, sender=models.CourierTravel)
def create_courier_travel(sender, instance, created, **kwargs):

    """
        This receiver updates daily and weekly income of a courier when
        a travel gets created
    """

    if created:
        with transaction.atomic():
            try:
                # Updates daily income
                courier_daily_income_rep = models_repositories.CourierDailyIncomeRepository()
                courier_daily_income_rep.update_income(date=instance.travel_date_time, income=instance.income,
                                                       courier=instance.courier)

                # Updates weekly income
                week_start_date = utils.get_week_start_date(instance.travel_date_time)
                courier_weekly_income_rep = models_repositories.CourierWeeklyIncomeRepository()
                courier_weekly_income_rep.update_income(date=week_start_date, income=instance.income,
                                                        courier=instance.courier)
            except Exception as e:
                # The transaction is rolled back if any error happens
                instance.delete()
                transaction.set_rollback(True)
                raise


@receiver(post_save, sender=models.CourierTransaction)
def create_courier_transaction(sender, instance, created, **kwargs):
    """
        This receiver updates daily and weekly income of a courier when a
        transaction gets created
    """

    if created:
        with transaction.atomic():
            try:
                # Updates daily income
                courier_daily_income_rep = models_repositories.CourierDailyIncomeRepository()
                courier_daily_income_rep.update_income(date=instance.date, income=instance.amount,
                                                       courier=instance.courier)

                # Updates weekly income
                week_start_date = utils.get_week_start_date(instance.date)
                courier_weekly_income_rep = models_repositories.CourierWeeklyIncomeRepository()
                courier_weekly_income_rep.update_income(date=week_start_date, income=instance.amount,
                                                        courier=instance.courier)
            except Exception as e:
                # The transaction is rolled back if any error happens
                instance.delete()
                transaction.set_rollback(True)
                raise



