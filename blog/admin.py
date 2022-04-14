from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Article)
class PersonAdmin(ImportExportModelAdmin):
	pass

@admin.register(Topic)
class PersonAdmin(ImportExportModelAdmin):
	pass

@admin.register(MSG)
class PersonAdmin(ImportExportModelAdmin):
	pass

@admin.register(Aboutme)
class PersonAdmin(ImportExportModelAdmin):
	pass

@admin.register(Banner)
class PersonAdmin(ImportExportModelAdmin):
	pass
