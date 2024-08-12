from django.urls import path
from .views import *

urlpatterns = [
    path('', DepartmentView.as_view(), name='department'),
    path('departments/<int:dep_id>/', EmployeeView.as_view(), name='emp'),

]
