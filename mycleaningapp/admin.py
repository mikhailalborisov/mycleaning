from django.contrib import admin
from .models import Employee, Home, Duty
from import_export import resources
from import_export.admin import ExportMixin

# Register your models here.
# admin.site.register(Employee)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")


# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "number_of_floors")
    search_fields = ("address", "number_of_floors")
    list_filter = ("address", "number_of_floors")


class DutyResource(resources.ModelResource):
    class Meta:
        model = Duty
        fields = ("id", "status", "home_id", "employee_id", "date_of_duty")


@admin.register(Duty)
class DutyAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("id", "status", "home_id", "employee_id", "date_of_duty")
    search_fields = ("status", "home_id", "employee_id", "date_of_duty")
    list_filter = ("status", "home_id", "employee_id", "date_of_duty")
