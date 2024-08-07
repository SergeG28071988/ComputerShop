from django.shortcuts import render, redirect
from .models import *
from .forms import ComponentForm
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
# Create your views here.


def index(request):
    return render(request, 'index.html')


def plot_component_prices(components):
    fig, ax = plt.subplots()

    component_names = [product.name for product in components]
    component_prices = [product.price for product in components]

    ax.bar(component_names, component_prices, color='lightcoral')
    plt.xlabel('Наименование товара')
    plt.ylabel('Цена товара')
    plt.title('Статистика цен на товары')
    plt.xticks(rotation=45)

    graph_file = BytesIO()
    plt.savefig(graph_file, format='png')
    graph_file.seek(0)

    graph_base64 = base64.b64encode(graph_file.read()).decode()

    plt.close('all')

    return graph_base64


def components(request):
    return render(request, 'component_list.html')


def add_component(request):
    return render(request, 'add_component.html')
