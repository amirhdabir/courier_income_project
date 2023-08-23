from rest_framework import serializers 
from incomes_handler_app import models


class CourierSerializer(serializers.ModelSerializer):

    """Serializer to serialize courier model data"""

    class Meta:
        model = models.Courier
        fields = '__all__'


class CourierWeeklyIncomeSerializer(serializers.ModelSerializer):

    """Serializer to serializer courier weekly income model data"""

    courier = CourierSerializer()

    class Meta:
        model = models.CourierWeeklyIncome
        fields = '__all__'
