import django_filters
from .models import UAV

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = UAV
        fields = {'id', 'brand', 'model', 'weight', 'category', 'rented' }