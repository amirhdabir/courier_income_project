from django.urls import path, include
from rest_framework.routers import DefaultRouter
from incomes_handler_app import views

app_name = "incomes_handler_app"
router = DefaultRouter()

urlpatterns = [
    path('couriers-weekly-incomes-list/',
         view=views.CourierWeeklyIncomeList.as_view(),
         name='couriers-weekly-incomes-list'),
]
