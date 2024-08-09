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
    components = Component.objects.all()
    context = {
        'components': components,
    }
    return render(request, 'component_list.html', context)


def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm()
    return render(request, 'add_component.html', {'form': form})


def price_statistics(request):
    name = request.GET.get('name')
    components = Component.objects.all()

    if name:
        components = components.filter(name__icontains=name)

    graph_base64 = plot_component_prices(components)
    context = {
        'graph_base64': graph_base64,
        'components': components,
        'header': f"Статистика цен для '{name}'" if name else "Статистика цен на товары"
    }
    return render(request, 'price_statistics.html', context)


def search_components(request):
    name = request.GET.get('name')
    components = Component.objects.filter(name__icontains=name)
    header = f"Найден товар '{name}'"
    context = {
        'components': components,
        'header': header
    }
    return render(request, 'component_list.html', context)


def print_components(request):
    components = Component.objects.all()
    return render(request, 'component_list.html', {'components': components})
