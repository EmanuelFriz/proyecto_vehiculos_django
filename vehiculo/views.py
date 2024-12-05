from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo_form.html', {'form': form})

def listar_vehiculos(request):
    if not request.user.is_authenticated:
        return redirect('index')
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.rango_precio = 'Bajo'
        elif 10001 <= vehiculo.precio <= 30000:
            vehiculo.rango_precio = 'Medio'
        else:
            vehiculo.rango_precio = 'Alto'
    return render(request, 'vehiculo_list.html', {'vehiculos': vehiculos})


def test_crispy(request):
    form = VehiculoForm()
    return render(request, 'test_crispy.html', {'form': form})
# Create your views here.