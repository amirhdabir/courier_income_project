from django_filters import rest_framework as filters
from incomes_handler_app import models


class DateRangeFilter(filters.FilterSet):

    """A filter class to filter between two dates"""

    from_date = filters.DateFilter(field_name='saturday_date', lookup_expr="gte")
    to_date = filters.DateFilter(field_name='saturday_date', lookup_expr="lte")
    
