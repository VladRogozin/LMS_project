from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView

from courses.forms import CreateCourseForm, UpdateCourseForm
from courses.models import Course
from django.urls import reverse, reverse_lazy


def get_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})


@login_required
def detail_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course/detail.html', {'title': 'Detail of group', 'course': course})


@login_required
def create_course_view(request):
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/create.html', {'form': form})


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


@login_required
def delete_course(request, pk):
    st = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('courses:list'))
    return render(request, 'courses/delete.html', {'course': st})