from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse
from cv_pdf.utils import render_to_pdf
from cv_to_pdf.models import *


class DepartmentList(ListView):
    model = Department
    template_name = 'cv_to_pdf/home.html'


class DepartmentView(DetailView):
    model = Department
    template_name = 'cv_to_pdf/department_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Department.objects.all()
        context['department'] = Department.objects.get(pk=kwargs['object'].pk)
        return context

class GeneratePDF(View):
    def get(self, request, template):
        pdf = render_to_pdf(template)
        return HttpResponse(pdf, content_type='application/pdf')
