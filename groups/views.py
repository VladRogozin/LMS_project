from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from groups.forms import CreateGroupForm, UpdateGroupForm
from groups.models import Group

from students.models import Student


class ListGroupView(ListView):
    model = Group
    template_name = 'groups/list.html'


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'title': 'Detail of group', 'group': group})


# def create_group_view(request):                        #
#     if request.method == 'GET':
#         form = CreateGroupForm()
#     elif request.method == 'POST':
#         form = CreateGroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#
#     return render(request, 'groups/create.html', {'form': form})


class CreateGroupView(CreateView):
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        new_group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()
        return response


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'POST':
        form = UpdateGroupForm(data=request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    form = UpdateGroupForm(instance=group, initial=students)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


class UpdateGroupView(UpdateView):
    model = Group
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            student.save()

        headman_pk = int(form.cleaned_data.get('headman_field'))
        if headman_pk:
            form.instance.headman = Student.objects.get(pk=headman_pk)
        else:
            form.instance.headman = None
        form.save()

        return response


def delete_group(request, pk):
    st = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'groups': st})