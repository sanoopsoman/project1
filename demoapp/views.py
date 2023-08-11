from django.shortcuts import render, redirect
from .models import tbl_staff, tbl_accounts, tbl_person, tbl_flower
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def demo(request):
    return render(request, 'demo.html')


def staff(request):
    return render(request, 'staff.html')


def accounts(request):
    return render(request, 'accounts.html')


def person(request):
    return render(request, 'person.html')


def add_staff(request):
    a1 = tbl_staff()
    a1.emp_id = request.POST.get('id')
    a1.name = request.POST.get('name')
    a1.des = request.POST.get('designation')
    a1.salary = request.POST.get('salary')
    a1.email = request.POST.get('email')
    a1.phone = request.POST.get('phno')
    a1.save()
    return render(request, 'staff.html')


def add_accounts(request):
    b1 = tbl_accounts()
    b1.emp_id = request.POST.get('id')
    b1.name = request.POST.get('name')
    b1.desig = request.POST.get('designation')
    b1.salary = request.POST.get('salary')
    b1.branch = request.POST.get('branch')
    b1.place = request.POST.get('place')
    b1.save()
    return render(request, 'accounts.html')


def add_person(request):
    c1 = tbl_person()
    c1.emp_name = request.POST.get('name')
    c1.salary = request.POST.get('no')
    c1.pf = request.POST.get('pf')
    c1.address = request.POST.get('adress')
    c1.exp = request.POST.get('exp')
    c1.status = request.POST.get('status')
    c1.save()
    return render(request, 'person.html')


def view_staff(request):
    d1 = tbl_staff.objects.all()
    return render(request, 'view_staff.html', {'data': d1})


def view_accounts(request):
    a1 = tbl_accounts.objects.all()
    return render(request, 'view_accounts.html', {'obj': a1})


def view_person(request):
    b1 = tbl_person.objects.all()
    return render(request, 'view_person.html', {'tbl': b1})


def update_staff(request, id):
    a1 = tbl_staff.objects.get(id=id)
    return render(request, 'update_staff.html', {'obj': a1})


def update_staff2(request, id):
    a1 = tbl_staff.objects.get(id=id)
    a1.emp_id = request.POST.get('id')
    a1.name = request.POST.get('name')
    a1.des = request.POST.get('designation')
    a1.salary = request.POST.get('salary')
    a1.email = request.POST.get('email')
    a1.phone = request.POST.get('phno')
    a1.save()
    return redirect('/view_staff')


def update_accounts(request, id):
    b1 = tbl_accounts.objects.get(id=id)
    return render(request, 'update_accounts.html', {'tbl': b1})


def update_accounts1(request, id):
    b1 = tbl_accounts.objects.get(id=id)
    b1.emp_id = request.POST.get('id')
    b1.name = request.POST.get('name')
    b1.desig = request.POST.get('designation')
    b1.salary = request.POST.get('salary')
    b1.branch = request.POST.get('branch')
    b1.place = request.POST.get('place')
    b1.save()
    return redirect('/view_accounts')


def update_person(request, id):
    z1 = tbl_person.objects.get(id=id)
    return render(request, 'update_person.html', {'data': z1})


def update_person2(request, id):
    c1 = tbl_person.objects.get(id=id)
    c1.emp_name = request.POST.get('name')
    c1.salary = request.POST.get('no')
    c1.pf = request.POST.get('pf')
    c1.address = request.POST.get('adress')
    c1.exp = request.POST.get('exp')
    c1.status = request.POST.get('status')
    c1.save()
    return redirect('/view_person')


def delete_accounts(request, id):
    a1 = tbl_accounts.objects.get(id=id)
    a1.delete()
    return redirect('/view_accounts')


def delete_person(request, id):
    b1 = tbl_person.objects.get(id=id)
    b1.delete()
    return redirect('/view_person')


def delete_staff(request, id):
    c1 = tbl_staff.objects.get(id=id)
    c1.delete()
    return redirect('/view_staff')


def view_salary(request):
    d1 = tbl_staff.objects.filter(salary__gte=15000)
    return render(request, 'view_staff.html', {'data': d1})


def flower(request):
    return render(request, 'flowers.html')


def add_flower(request):
    a1 = tbl_flower()
    a1.name = request.POST.get('name')
    image = request.FILES['image']
    obj = FileSystemStorage()
    data = obj.save(image.name, image)
    i = obj.url(data)
    a1.img = i
    a1.price = request.POST.get('price')
    a1.save()
    return redirect('/')
