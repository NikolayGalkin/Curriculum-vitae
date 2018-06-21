import factory
from .models import *


class EducationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Education

    place = 'Test place'
    specialization = 'Test specialization'
    year_of_ending = 2007
    index = 0


class CommunicationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Communication

    description = 'Test description'
    index = 0


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project

    is_nda = False
    project_title = 'Test project title'
    nda_title = 'Test nda title'
    description = 'Test description'
    team = 'Test team'
    role = 'Test role'
    skills = 'Test skills'


class ToolAndFrameworkFactory(factory.DjangoModelFactory):
    class Meta:
        model = ToolAndFramework

    name = 'Test'
    description = 'Test Description'
    index = 0


class TechnicalExpertiseFactory(factory.DjangoModelFactory):
    class Meta:
        model = TechnicalExpertise

    description = 'Test description'
    index = 0


class ResumeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Resume

    role = 'Test_role'
    tech_exp = factory.RelatedFactory(TechnicalExpertiseFactory, 'resume')
    tool_frame = factory.RelatedFactory(ToolAndFrameworkFactory, 'resume')
    project = factory.RelatedFactory(ProjectFactory, 'resume')
    communication = factory.RelatedFactory(CommunicationFactory, 'resume')
    education = factory.RelatedFactory(EducationFactory, 'resume')


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = 'Test1'
    last_name = 'Test2'
    role = 'Junior'
    resume = factory.RelatedFactory(ResumeFactory, 'person')


class GroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = Group

    group_name = 'Test_group'
    person = factory.RelatedFactory(PersonFactory, 'group')


class DepartmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Department

    dep_name = 'Test_department'
    department = factory.RelatedFactory(GroupFactory, 'department')
