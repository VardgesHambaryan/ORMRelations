from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    department_id = models.ForeignKey("Department", on_delete=models.PROTECT, related_name='emp_dep') 


    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    class Meta:
        db_table = 'employee'
        verbose_name_plural = 'Employes'

class Department(models.Model):
    address = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.specialization
    
    class Meta:
        db_table = 'department'
        verbose_name_plural = 'Department'

class Chair(models.Model):

    chair_number = models.PositiveSmallIntegerField()
    employee_id = models.OneToOneField("Employee", on_delete=models.PROTECT, related_name='emp_chair')

    def __str__(self) -> str:
        return f"{self.chair_number}"

    class Meta:
        db_table = 'chair'
        verbose_name_plural = 'Chair'






class SmartShoes(models.Model):

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color_id = models.ManyToManyField("Color")

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

    class Meta:
        db_table = "smart_shoes"
        verbose_name_plural = "SmartShoes"

class Color(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "color"