from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from webargs.djangoparser import use_args
from Teachers.forms import CreateTeacherForm, UpdateTeacherForm, TeacherFilterForm
from webargs.fields import Str
from .models import Teacher
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class CreateTeacherView(CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/create.html'


class UpdateTeacherView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'


class DeleteTeacherView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'