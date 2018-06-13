from django.urls import path

from cv_to_pdf.views import *

app_name = 'cv'

urlpatterns = [
    path('home/', DepartmentList.as_view(), name='department'),
    path('home/department_<int:pk>/', DepartmentView.as_view(), name='department_detail'),
    path('home/department_<int:pk>/group_<int:group_id>/', GroupView.as_view(), name='group_detail'),
    path('home/department_<int:pk>/group_<int:group_id>/<int:person>/', PersonView.as_view(), name='person_detail'),
    path('home/department_<int:pk>/group_<int:group_id>/<int:person>/<int:resume>/', ResumeView.as_view(), name='resume_detail'),
    path('test/test_pdf/', GeneratePDF.as_view(), name='test_pdf'),
]
