import django_filters

from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    authors = django_filters.CharFilter(lookup_expr='icontains')
    published__gt = django_filters.NumberFilter(field_name='published_date', lookup_expr='gt')
    published__lt = django_filters.NumberFilter(field_name='published_date', lookup_expr='lt')

    class Meta:
        model = Book
        fields = ['title', 'authors', 'language', 'published__gt', 'published__lt']
