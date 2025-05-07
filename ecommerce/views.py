from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ProductoForm
import requests

FIREBASE_BASE_URL = 'https://wiki-11737-default-rtdb.firebaseio.com/ecommerce'

def home(request): 
    response = requests.get(f'{FIREBASE_BASE_URL}.json')
    data = response.json() or {}

    productos = []
    for key, value in data.items():
        productos.append({
            'id': key,
            'nombre': value.get('nombre'),
            'descripcion': value.get('descripcion'),
            'precio': value.get('precio'),
        })

    productos.reverse()
    return render(request, 'home.html', {'productos': productos})

def formulario_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            data = {
                'nombre': form.cleaned_data['nombre'],
                'descripcion': form.cleaned_data['descripcion'],
                'precio': float(form.cleaned_data['precio']),
            }
            requests.post(f'{FIREBASE_BASE_URL}.json', json=data)
            return redirect('home')
    else:
        form = ProductoForm()

    return render(request, 'forms.html', {'form': form})