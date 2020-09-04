from .models import Lomba, Kategori
import django_filters
from django import forms

class Filter(django_filters.FilterSet):
    
    CHOICES1={
        ('ascending', 'Ascending'),
        ('descending', 'Descending'),
    }
    CHOICES2={
        (False, 'Aktif'),
        (True, 'Tidak Aktif')
    }

    COMP_LEVEL = (
        ("lokal","Lokal"),
        ("nasional","Nasional"),
        ("internasional","Internasional")
    )

    PARTI_LEVEL = (
        ("sd","SD"),
        ("smp","SMP"),
        ("sma","SMA"),
        ("univ","Universitas"),
        ("umum","Umum")
    )
    competitions_level = django_filters.MultipleChoiceFilter(choices=COMP_LEVEL,widget=forms.CheckboxSelectMultiple)
    
    participant_level = django_filters.MultipleChoiceFilter(choices=PARTI_LEVEL,widget=forms.CheckboxSelectMultiple)
    category = django_filters.ModelMultipleChoiceFilter(queryset=Kategori.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    ordering = django_filters.ChoiceFilter(label='Ordering',widget=forms.RadioSelect, choices=CHOICES1, method='filter_by_order', empty_label=None)
    
    active = django_filters.BooleanFilter(field_name='active', lookup_expr='isnull',widget=forms.Select(choices=CHOICES2))
    name = django_filters.CharFilter(field_name='name', widget=forms.Textarea, lookup_expr='icontains' )

    class Meta:
        model = Lomba
        fields = ['name','category', 'ordering','participant_level','competitions_level','active']

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)

