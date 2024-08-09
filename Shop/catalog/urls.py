from django.urls import path
from .views import index, components, add_component, price_statistics, search_components, print_components

urlpatterns = [
    path('', index, name="index"),
    path('components/', components, name="component_list"),
    path('add_component/', add_component, name="add_component"),
    path('price-statistics/', price_statistics, name='price_statistics'),  # новый маршрут
    path('search/', search_components, name='search_components'),
    path('print_components/', print_components, name='print_components'),
]
