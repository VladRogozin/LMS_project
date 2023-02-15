from django import forms
from django_filters import FilterSet

from courses.models import Course
from groups.models import Group


class CourseBaseForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def save(self, commit=True):
        new_course = super().save(commit)
        groups = self.cleaned_data['groups']
        for group in groups:
            group.group = new_course
            group.save()

    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'course_start': forms.DateInput(attrs={"type": 'date'})
        }


class CreateCourseForm(CourseBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.filter(course__isnull=True).select_related('course')

    class Meta(CourseBaseForm.Meta):
        pass


class UpdateCourseForm(CourseBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all().select_related('course')

    class Meta(CourseBaseForm.Meta):
        exclude = [
            'start_date'
        ]


class CourseFilterForm(FilterSet):

    class Meta:
        model = Course
        fields = {
            'name': ['exact', 'icontains', 'startswith']
        }