from django.contrib import admin
from incomes_handler_app import models

@admin.register(models.Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.CourierTravel)
class CourierTravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin_distance', 'travel_distance', 'customer_type',
                    'travel_date_time', 'income', 'courier')
    search_fields = ('courier__name',)


@admin.register(models.CourierTransactionReason)
class CourierTransactionReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason')


@admin.register(models.CourierTransaction)
class CourierTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'reason', 'courier')
    search_fields = ('reason__reason', 'courier__name',)


@admin.register(models.CourierDailyIncome)
class CourierDailyIncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'income', 'courier')
    search_fields = ('courier__name',)


@admin.register(models.CourierWeeklyIncome)
class CourierWeeklyIncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'saturday_date', 'income', 'courier')
    search_fields = ('courier__name',)