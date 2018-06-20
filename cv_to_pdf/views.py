from __future__ import unicode_literals
# from weasyprint import HTML
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse
from cv_to_pdf.models import *


class BaseView(ListView):
    model = Department
    template_name = 'cv_to_pdf/home_page.html'


class DepartmentDetail(DetailView):
    model = Department
    template_name = 'cv_to_pdf/department_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Department.objects.all()
        context['department'] = Department.objects.get(pk=kwargs['object'].pk)
        return context


class GroupDetail(DetailView):
    model = Group
    template_name = 'cv_to_pdf/group_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Department.objects.all()
        context['department'] = Department.objects.get(pk=kwargs['object'].department.pk)
        # context['group'] = Group.objects.get(pk=kwargs['object'].pk)
        return context

    def get_object(self, queryset=None):
        obj = Group.objects.get(pk=self.kwargs['group_id'])
        return obj


class PersonDetail(DetailView):
    model = Person
    template_name = 'cv_to_pdf/person_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Department.objects.all()
        context['department'] = Department.objects.get(pk=kwargs['object'].group.department.pk)
        context['group'] = Group.objects.get(pk=kwargs['object'].group.pk)
        return context

    def get_object(self, queryset=None):
        obj = Person.objects.get(pk=self.kwargs['person'])
        return obj


class ResumeDetail(DetailView):
    models = Resume
    template_name = 'cv_to_pdf/resume_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = Department.objects.get(pk=kwargs['object'].person.group.department.pk)
        context['group'] = Group.objects.get(pk=kwargs['object'].person.group.pk)
        context['person'] = Person.objects.get(pk=kwargs['object'].person.pk)
        return context

    def get_object(self, queryset=None):
        obj = Resume.objects.get(pk=self.kwargs['resume'])
        return obj


class ResumeView(DetailView):
    models = Resume
    template_name = 'cv_to_pdf/resume_detail.html'

    def get_object(self, queryset=None):
        obj = Resume.objects.get(pk=self.kwargs['resume'])
        return obj


# class GeneratePDF(View):
#     def render_pdf(self, **kwargs):
#         html = HTML('http://127.0.0.1:8000/home/department_' +
#                     str(kwargs['pk']) + '/group_' + str(kwargs['group_id']) + '/' +
#                     str(kwargs['person']) + '/' + str(kwargs['resume']) + '/').write_pdf()
#         response = HttpResponse(html, content_type='application/pdf')
#         return response
