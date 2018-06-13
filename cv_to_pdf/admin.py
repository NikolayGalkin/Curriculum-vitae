from __future__ import unicode_literals
from django.contrib import admin

from cv_to_pdf.models import *


class GroupInline(admin.TabularInline):
    model = Group


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        GroupInline
    ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Resume)
admin.site.register(TechnicalExpertise)
admin.site.register(ToolAndFramework)
admin.site.register(Project)
admin.site.register(Communication)
admin.site.register(Education)