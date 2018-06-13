from django.urls import path

from cv_to_pdf.views import *

app_name = 'cv'

urlpatterns = [
    path('departments/', DepartmentList.as_view(), name='department'),
    path('departments/<pk>/', DepartmentView.as_view(), name='department_detail'),
    path('test/test_pdf/', GeneratePDF.as_view(), name='test_pdf'),
]