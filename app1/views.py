from django.shortcuts import render, redirect

from .forms import EmployeeForm
from .models import Employee


def emp_create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_url')

    return render(request, 'app1/emp_form.html', {'form': form})


def emp_list_view(request):
    objs = Employee.objects.all()

    return render(request, 'app1/emp_list.html', {'objs': objs})


def emp_update_view(request, pk):
    obj = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list_url')

    return render(request, 'app1/emp_form.html', {'form': form})


def emp_delete_view(request, pk):
    obj = Employee.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('list_url')

    return render(request, 'app1/delete.html', {'obj': obj})
