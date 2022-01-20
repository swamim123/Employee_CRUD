from django.shortcuts import render
from emp_reg.models import Employee
# Create your views here.

from datetime import datetime


def welcome_page(request):
    return render(request, template_name="employee.html")


def save_update_employees(request):
    error_message = ''
    success_message = ''
    if request.method == 'POST':
        formdata = request.POST
        print('FORMDATA : ', formdata)
        eid = formdata.get('eid')
        enm = formdata.get('enm')
        if not enm:
            error_message = "Employee Name Cannot be Empty...!"
        else:
            eage = formdata.get('eage')
            erole = formdata.get('role')
            email = formdata.get('eemail')
            edj = formdata.get('edate')  # str -- Date mein---user entered date
            edr = formdata.get('address')
            ephone = formdata.get('ephone')
            # currentDate = datetime.now()
            parts = edj.split("/")  # 24/12/2021
            # currentDate.day = parts[0]  #24
            # currentDate.month = parts[1] #12
            # currentDate.year = parts[2] #2021
            edj = datetime(int(parts[2]), int(parts[1]), int(parts[0]))

            emp = Employee(name=enm, age=eage, email=email, role=erole, phone_num=ephone,
                           joiningDate=edj, address=edr)
            emp.save()
            success_message = "Employee Record Saved..!"
        return render(request, "employee.html", {"success_message": success_message, "error_message": error_message})


def edit_employee(request):
    pass


def delete_employee(request):
    pass


# from django.shortcuts import render

# Create your views here.
