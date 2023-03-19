import django_filters
from django import forms
from .models import *
from django_filters import NumberFilter



class ListingFilter(django_filters.FilterSet):
    availability = django_filters.ModelChoiceFilter(
        queryset=availability.objects.all(),
        empty_label="All Categories",
        label="Availability",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    buyer = django_filters.ModelChoiceFilter(
        queryset=buyer.objects.all(),
        empty_label="All Categories",
        label="Buyer category",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    category = django_filters.ModelChoiceFilter(
        queryset=category.objects.all(),
        empty_label="All Categories",
        label="Categories",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    size = django_filters.ModelChoiceFilter(
        queryset=size.objects.all(),
        empty_label="All Categories",
        label="Size",
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    color = django_filters.ModelChoiceFilter(
        queryset=color.objects.all(),
        empty_label="All Categories",
        label="Color",
        widget=forms.Select(attrs={'class': 'form-control',}),
        )
    min_price = NumberFilter(field_name='price', lookup_expr='gte',label="Min Price",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price = NumberFilter(field_name='price', lookup_expr='lte',label="Max Price",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields=['buyer','category','color','size','min_price','max_price','availability']



    