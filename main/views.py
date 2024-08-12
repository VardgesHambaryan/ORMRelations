from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class DepartmentView(ListView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        departments = Department.objects.all()

        context = {
            "departments":departments,
        }
        return render(request, self.template_name, context=context)
    

class EmployeeView(ListView):
    template_name='emp.html'

    def get(self, request: HttpRequest, dep_id, *args: Any, **kwargs: Any) -> HttpResponse:
        
        departments = Department.objects.filter(pk=dep_id)
        

        context = {
            "departments":departments,
        }
        return render(request, self.template_name, context=context)
    
