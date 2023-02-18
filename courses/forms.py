from django import forms
from django_filters import FilterSet

from courses.models import Course

"""
Не уверен может быть create и update нужно было в один класс и наследоватьс,
или же заменить их одним 
оставлю так пока
"""


class CreateCourseForm:
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'course_start': forms.DateInput(attrs={"type": 'date'})
        }


class UpdateCourseForm:
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'course_start': forms.DateInput(attrs={"type": 'date'})
        }


class CourseFilterForm(FilterSet):

    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains', 'startswith']
        }