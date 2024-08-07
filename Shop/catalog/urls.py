from django.urls import path
from .views import index, components, add_component

urlpatterns = [
    path('', index, name="index"),
    path('components/', components, name="component_list"),
    path('add_component/', add_component, name="add_product"),
]
