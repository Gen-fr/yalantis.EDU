import django_filters
from .models import Driver

class DrvFilter(django_filters.FilterSet):
    created_at__gt = django_filters.NumberFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Driver
        fields = {
            'created_at': ['lte', 'gte'],
        }

