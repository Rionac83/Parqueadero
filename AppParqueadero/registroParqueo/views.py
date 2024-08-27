from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Autos
from .forms import AddClienteForm, EditarClienteForm, AddAutomovilForm, EditarAutomovilForm, imprimirTicketForm
from django.contrib import messages

# Create your views here.

def registroParqueo(request):
    autos = Autos.objects.all()
    form_auto = AddAutomovilForm()
    form_editar = EditarAutomovilForm()
    form_ticket = imprimirTicketForm()
    context = {
        'autos': autos,
        'form_auto': form_auto,
        'form_editar': form_editar,
        'form_ticket_auto': form_ticket,
    }
    return render(request,'registroParqueo.html',context)

def clientes(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
        
    }
    return render(request,'clientes.html',context)

def add_clientes(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al guardar el cliente")
                return redirect('cliente')
    return redirect('cliente')

def edit_clientes(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
        request.POST, request.FILES, instance = cliente)
        if form.is_valid:
            form.save()
    return redirect('cliente')

def delete_clientes(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('cliente')

def add_automovil(request):
    if request.POST:
        form = AddAutomovilForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al Guardar el Auto")
                return redirect('registroParqueo')
    return redirect('registroParqueo')

def edit_automovil(request):
    if request.POST:
        automovil = Autos.objects.get(pk=request.POST.get('id_automovil_editar'))
        form = EditarAutomovilForm(
        request.POST, request.FILES, instance = automovil)
        if form.is_valid:
            form.save()
    return redirect('registroParqueo')

def delete_automovil(request):
    if request.POST:
        auto = Autos.objects.get(pk=request.POST.get('id_automovil_eliminar'))
        auto.delete()
    return redirect('registroParqueo')

def imprimir_ticket(request, pk):
    auto = Autos.objects.get(pk=pk)
    form = imprimirTicketForm(initial={
        'horaEntrada': auto.horaEntrada.strftime('%Y-%m-%dT%H:%M'),
        'horaSalida': auto.horaSalida.strftime('%Y-%m-%dT%H:%M')
    })
    return redirect(request, 'registroParqueo', {'form': form})
    
    






