from django.shortcuts import render
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def libros(request):
    return render(request, "libros.html")

def destacados(request):
    return render(request, "destacados.html")

def reseñas(request):
    return render(request, "reseñas.html")

def iniciar_sesion(request):
    return render(request, "iniciar_sesion.html")

def buscar_libros_por_autor(request):
    if request.method == 'POST':
        autor_id = request.POST.get('autor_id')
        libros = Libro.objects.filter(autor_id=autor_id)
    else:
        libros = Libro.objects.all()
    return render(request, 'buscar_libros.html', {'libros': libros})

def buscar_libros_por_genero(request):
    if request.method == 'POST':
        genero_id = request.POST.get('genero_id')
        libros = Libro.objects.filter(genero__id=genero_id)
    else:
        libros = Libro.objects.all()
    return render(request, 'buscar_libros.html', {'libros': libros})
