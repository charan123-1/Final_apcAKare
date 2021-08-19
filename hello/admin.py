from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Guntur,EG,WG,Krishna,Prakasam,Ananthapur,Kurnool,Visakha,Vizianagaram,Srikakulam,Kadapa,Chittoor,Nellore
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Guntur)
class excelSheet(ImportExportModelAdmin):
    pass
@admin.register(EG)
class excelSheet(ImportExportModelAdmin):
    pass


@admin.register(WG)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Krishna)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Prakasam)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Ananthapur)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Kurnool)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Visakha)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Vizianagaram)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Srikakulam)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Kadapa)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Chittoor)
class excelSheet(ImportExportModelAdmin):
    pass

@admin.register(Nellore)
class excelSheet(ImportExportModelAdmin):
    pass