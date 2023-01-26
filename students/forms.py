from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'city',
            'phone',
        ]

    def clean_phone(self):
        value = self.cleaned_data.get('phone')

        return ''.join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','(',')','-','+'], value))

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.capitalize()
