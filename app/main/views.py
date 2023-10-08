from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView





class SensorDetailView(DetailView):
    model = Sensor
    template_name = 'main/details_view.html'
    context_object_name = 'sensor'


class SensorUpdateView(UpdateView):
    model = Sensor
    template_name = 'main/add_sensor.html'
    form_class = SensorForm


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'main/update_category.html'
    form_class = CategoryForm


class EngUpdateView(UpdateView):
    model = EngUnits
    template_name = 'main/update_eng.html'
    form_class = CategoryForm


class SensorDeleteView(DeleteView):
    model = Sensor
    success_url = '/'
    template_name = 'main/delete_sensor.html'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/add_cat'
    template_name = 'main/delete_category.html'


class EngDeleteView(DeleteView):
    model = EngUnits
    success_url = '/add_engunits'
    template_name = 'main/delete_eng.html'


def about(request):
    return render(request, 'main/about.html')


def index(request):
    cat = Category.objects.all()
    sensor = Sensor.objects.all()

    if request.method == 'POST':
        namecat = request.POST.get('name_cat')
        try:
            category = Category.objects.get(name=namecat)
            sensor = Sensor.objects.filter(cat=category.id)
        except Category.DoesNotExist:
            pass

    if request.method == 'GET':
        namesensor = request.GET.get('namesensor')
        if namesensor != None:
            print(namesensor)
            try:
                sensor = Sensor.objects.filter(position=namesensor)
            except Category.DoesNotExist:
                pass

    data = {
        'sensor': sensor,
        'cat': cat
    }

    return render(request, 'main/index.html', data)



def add(request):
    error = ''
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверные данные'

    form = SensorForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_sensor.html', data)


def add_engunits(request):
    error = ''
    if request.method == 'POST':
        form = EngUnitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_engunits')
        else:
            error = 'Неверные данные'

    form = EngUnitsForm()
    engunits = EngUnits.objects.all()
    data = {
        'form': form,
        'error': error,
        'engunits': engunits
    }
    return render(request, 'main/add_engunits.html', data)


def add_cat(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_cat')
        else:
            error = 'Неверные данные'

    form = CategoryForm()
    category = Category.objects.all()
    data = {
        'form': form,
        'error': error,
        'category': category
    }
    return render(request, 'main/add_category.html', data)




