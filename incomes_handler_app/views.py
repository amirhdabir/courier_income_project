from rest_framework import generics
from django_filters import rest_framework as filters
from incomes_handler_app import models
from incomes_handler_app import serializers
from incomes_handler_app import custom_filters


class CourierWeeklyIncomeList(generics.ListAPIView):

    """Lists the courier weekly incomes in a specific date range"""

    queryset = models.CourierWeeklyIncome.objects.all()
    serializer_class = serializers.CourierWeeklyIncomeSerializer
    filterset_class = custom_filters.DateRangeFilter
    filter_backends = (filters.DjangoFilterBackend,)



