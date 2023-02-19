from django import forms
from django_filters import FilterSet

from groups.models import Group
from students.models import Student


class GroupBaseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)

    # def save(self, commit=True):
    #     new_group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = new_group
    #         student.save()

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_start': forms.DateInput(attrs={"type": 'date'})
        }


class CreateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True).select_related('group')

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'headman',
        ]


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all().select_related('group')
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False
        )
        self.fields['headman_field'].choices.insert(0, (0, '----------'))

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
            'headman'
        ]


class GroupFilterForm(FilterSet):

    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains', 'startswith']
        }