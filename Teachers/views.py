from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from Teachers.forms import CreateTeacherForm, UpdateTeacherForm, TeacherFilterForm
from webargs.fields import Str
from .models import Teacher
from .utils import format_list_teachers


def get_teachers(request):                #
    teachers = Teacher.objects.all().order_by('salary')

    filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'filter_form': filter_form
        }
    )


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'title': 'Detail of teacher','teacher': teacher})


def create_teacher_view(request):                     #
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/create.html', {'form': form})


def update_teacher(request, pk):                      #
    teacher = get_object_or_404(Teacher, pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, pk):
    st = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request, 'teachers/delete.html', {'teacher': st})