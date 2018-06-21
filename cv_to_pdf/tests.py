from django.test import TestCase
from .factories import *
from django.urls import reverse


class DepartmentTestCase(TestCase):
    def setUp(self):
        self.department = DepartmentFactory()

    def test_get_groups(self):
        department = self.department
        self.assertEqual(len(department.get_groups()), 1)

    def test_get_groups_count(self):
        department = self.department
        self.assertEqual(department.get_groups_count(), 1)

    def test_get_group_employees(self):
        group = self.department.get_groups()[0]
        self.assertEqual(len(group.get_employees()), 1)

    def test_get_group_employees_count(self):
        group = self.department.get_groups()[0]
        self.assertEqual(group.get_employees_count(), 1)

    def test_get_person_full_name(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        self.assertEqual(person.get_full_name(), person.first_name + ' ' + person.last_name)

    def test_get_person_resume(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        self.assertEqual(len(person.get_resume()), 1)

    def test_get_person_resume_count(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        self.assertEqual(person.get_resume_count(), 1)

    def test_get_resume_technical_expertise(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        resume = person.get_resume()[0]
        self.assertEqual(len(resume.get_technical_expertise()), 1)

    def test_get_resume_tool_and_frameworks(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        resume = person.get_resume()[0]
        self.assertEqual(len(resume.get_tool_and_framework()), 1)

    def test_get_resume_project(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        resume = person.get_resume()[0]
        self.assertEqual(len(resume.get_project()), 1)

    def test_get_resume_communication(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        resume = person.get_resume()[0]
        self.assertEqual(len(resume.get_communication()), 1)

    def test_get_resume_education(self):
        group = self.department.get_groups()[0]
        person = group.get_employees()[0]
        resume = person.get_resume()[0]
        self.assertEqual(len(resume.get_education()), 1)
