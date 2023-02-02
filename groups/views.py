from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str
from django.db.models import Q

from groups.forms import CreateGroupForm, UpdateGroupForm
from groups.models import Group
from groups.utils import format_list_groups


@use_args(                                             #
    {
        'group_name': Str(required=False),
    },
    location='query',
)
def get_groups(request, args):                         #
    groups = Group.objects.all().order_by('group_start')

    if len(args) and args.get('group_name'):
        groups = groups.filter(
            Q(group_name=args.get('group_name', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={'title': 'List of Groups', 'groups': groups}
    )


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'title': 'Detail of group','group': group})


def create_group_view(request):                        #
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def update_group(request, pk):                   #
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_group(request, pk):
    st = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request, 'groups/delete.html', {'groups': st})