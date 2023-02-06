from django import forms
from django_filters import FilterSet

from groups.models import Group


class CreateGroupForm(forms.ModelForm):        #
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start',
            'group_text',
        ]
        widgets = {
            'group_start': forms.DateInput(attrs={"type": 'date'})
        }


class UpdateGroupForm(forms.ModelForm):                          #
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start',
            'group_text',
        ]
        widgets = {
            'group_start': forms.DateInput(attrs={"type": 'date'})
        }


class GroupFilterForm(FilterSet):

    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains', 'startswith']
        }