from __future__ import unicode_literals
from django.contrib import admin

from cv_to_pdf.models import *


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        GroupInline,
    ]


class TechnicalExpertiseInline(admin.TabularInline):
    model = TechnicalExpertise
    extra = 1


class ToolAndFrameworkInline(admin.TabularInline):
    model = ToolAndFramework
    extra = 1


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1


class CommunicationInline(admin.TabularInline):
    model = Communication
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class ResumeAdmin(admin.ModelAdmin):
    inlines = [
        TechnicalExpertiseInline,
        ToolAndFrameworkInline,
        ProjectInline,
        CommunicationInline,
        EducationInline,
    ]


class PersonInline(admin.TabularInline):
    model = Person
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        PersonInline,
    ]


class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        ResumeInline,
    ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(TechnicalExpertise)
admin.site.register(ToolAndFramework)
admin.site.register(Project)
admin.site.register(Communication)
admin.site.register(Education)
