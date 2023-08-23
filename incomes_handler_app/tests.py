from django.test import TestCase
from django.db.models import Sum
from incomes_handler_app import models
from datetime import date


class IncomeAggregationTestCase(TestCase):

    """Tests couriers daily income aggregation from travels and transactions"""
    
    def setUp(self):
        """Prepares needed data for the test"""
        
        # A customer type and a transaction reason is needed
        customer_type = models.CustomerType.objects.create(name='customer_type')
        transaction_reason = models.CourierTransactionReason.objects.create(reason='reason')

        # Two couriers are considered for test
        couriers = [
            models.Courier(name='courier_1'),
            models.Courier(name='courier_2')
            ]
        models.Courier.objects.bulk_create(couriers)

        # Courier's incomes and their details should be set by date
        # For courier 1
        travel_incomes_1 = [50, 20.8]
        transaction_incomes_1 = [5.5 , -10, 25]
        self.courier_1_today_income = travel_incomes_1[0] + transaction_incomes_1[0] + transaction_incomes_1[1]
        self.courier_1_another_day_income = travel_incomes_1[1] + transaction_incomes_1[2]
        # For courier 2
        travel_incomes_2 = [30.1, 40]
        transaction_incomes_2 = [-5 , 20.6, -5]
        self.courier_2_today_income = travel_incomes_2[0] + transaction_incomes_2[0] + transaction_incomes_2[1]
        self.courier_2_another_day_income = travel_incomes_2[1] + transaction_incomes_2[2]

        # Dates should be set
        self.today = date.today()
        self.another_day_date = date(2023,10,10)

        # Some courier travels are needed with different dates for couriers
        courier_travels = [
            models.CourierTravel(
                                origin_distance=0, travel_distance=0, customer_type=customer_type,
                                income=travel_incomes_1[0], travel_date_time=self.today, courier=couriers[0]
                                ),
            models.CourierTravel(
                                origin_distance=0, travel_distance=0, customer_type=customer_type,
                                income=travel_incomes_1[1], travel_date_time=self.another_day_date, courier=couriers[0]
                                ),
            models.CourierTravel(
                                origin_distance=0, travel_distance=0, customer_type=customer_type,
                                income=travel_incomes_2[0], travel_date_time=self.today, courier=couriers[1]
                                ),
            models.CourierTravel(
                                origin_distance=0, travel_distance=0, customer_type=customer_type,
                                income=travel_incomes_2[1], travel_date_time=self.another_day_date, courier=couriers[1]
                                ),
        ]
        models.CourierTravel.objects.bulk_create(courier_travels)

        # Some courier transactions are needed with different dates for couriers
        courier_transactions = [
            models.CourierTransaction(
                                      amount=transaction_incomes_1[0], reason=transaction_reason,
                                      courier=couriers[0], date=self.today
                                      ),
            models.CourierTransaction(
                                      amount=transaction_incomes_1[1], reason=transaction_reason,
                                      courier=couriers[0], date=self.today
                                      ),
            models.CourierTransaction(
                                      amount=transaction_incomes_1[2], reason=transaction_reason,
                                      courier=couriers[0], date=self.another_day_date
                                      ),
            models.CourierTransaction(
                                      amount=transaction_incomes_2[0], reason=transaction_reason,
                                      courier=couriers[1], date=self.today
                                      ),
            models.CourierTransaction(
                                      amount=transaction_incomes_2[1], reason=transaction_reason,
                                      courier=couriers[1], date=self.today
                                      ),
            models.CourierTransaction(
                                      amount=transaction_incomes_2[2], reason=transaction_reason,
                                      courier=couriers[1], date=self.another_day_date
                                      ),
            ]
        models.CourierTransaction.objects.bulk_create(courier_transactions)

    def test_today_income_aggregation(self):
        """
            The first courier's income of today should be aggregated
            and compared with the value it should be
        """

        # Test for the first courier
        travel_total_income_1 = models.CourierTravel.objects.filter(
            courier__id=1, travel_date_time=self.today
            ).aggregate(total_income=Sum("income"))["total_income"]
        transactions_travel_total_income_1 = models.CourierTransaction.objects.filter(
            courier__id=1, date=self.today
            ).aggregate(total_income=Sum("amount"))["total_income"]
        total_income_1 = travel_total_income_1 + transactions_travel_total_income_1
        self.assertEqual(total_income_1, self.courier_1_today_income)

        # Test for the second courier
        travel_total_income_2 = models.CourierTravel.objects.filter(
            courier__id=2, travel_date_time=self.today
            ).aggregate(total_income=Sum("income"))["total_income"]
        transactions_travel_total_income_2 = models.CourierTransaction.objects.filter(
            courier__id=2, date=self.today
            ).aggregate(total_income=Sum("amount"))["total_income"]
        total_income_2 = travel_total_income_2 + transactions_travel_total_income_2
        self.assertEqual(total_income_2, self.courier_2_today_income)
    
    def test_another_day_income_aggregation(self):
        """
            The first courier's income of another date besides today should be aggregated
            and compared with the value it should be
        """

        # Test for the first courier
        travel_total_income_1 = models.CourierTravel.objects.filter(
            courier__id=1, travel_date_time=self.another_day_date
            ).aggregate(total_income=Sum("income"))["total_income"]
        transactions_travel_total_income_1 = models.CourierTransaction.objects.filter(
            courier__id=1, date=self.another_day_date
            ).aggregate(total_income=Sum("amount"))["total_income"]
        total_income_1 = travel_total_income_1 + transactions_travel_total_income_1
        self.assertEqual(total_income_1, self.courier_1_another_day_income)

        # Test for the second courier
        travel_total_income_2 = models.CourierTravel.objects.filter(
            courier__id=2, travel_date_time=self.another_day_date
            ).aggregate(total_income=Sum("income"))["total_income"]
        transactions_travel_total_income_2 = models.CourierTransaction.objects.filter(
            courier__id=2, date=self.another_day_date
            ).aggregate(total_income=Sum("amount"))["total_income"]
        total_income_2 = travel_total_income_2 + transactions_travel_total_income_2
        self.assertEqual(total_income_2, self.courier_2_another_day_income)
        

