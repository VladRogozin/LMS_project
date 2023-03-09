from django.contrib import admin
from django import forms
from groups.models import Group


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    extra = 1
    verbose_name = 'teacher'
    filter = ('teacher_first_name', 'teacher_last_name', 'teacher_salary')
    readonly_fields = filter

    def teacher_first_name(self, instance):
        return instance.teacher.first_name
    teacher_first_name.short_description = 'First name'

    def teacher_last_name(self, instance):
        return instance.teacher.last_name
    teacher_last_name.short_description = 'Last name'

    def teacher_salary(self, instance):
        return instance.teacher.salary
    teacher_salary.short_description = 'salary'

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class StudentsInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email', 'birthday', 'created', 'updated')
    extra = 0
    readonly_fields = fields
    # show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman'].choices = [(s.pk, f'{s.first_name} {s.last_name}') for s in self.instance.students.all()]
        self.fields['headman'].choices.insert(0, (0, '------'))

        self.fields['headman'].widget.can_add_related = False
        self.fields['headman'].widget.can_change_related = False
        self.fields['headman'].widget.can_view_related = False
        self.fields['headman'].widget.can_delete_related = False

    class Meta:
        model = Group
        fields = '__all__'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ('group_name', 'group_start', 'group_text')
    fields = (
        'group_name',
        'group_start',
        'group_text',
        'headman',

    )

    inlines = (StudentsInlineTable, TeachersInlineTable)
