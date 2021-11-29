import django_filters
from .models import Computer

class ComputerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Computer
        fields = ["brand", "owner", "serial_number", "comp_type"]
