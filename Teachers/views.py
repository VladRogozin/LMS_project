from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from webargs.djangoparser import use_args
from Teachers.forms import CreateTeacherForm, UpdateTeacherForm
from webargs.fields import Str
from .models import Teacher
from .utils import format_list_teachers


def index(request):
    return HttpResponse('Welcome')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_teachers(request, args):
    teachers = Teacher.objects.all().order_by('salary')

    if len(args) and (args.get('first_name') or args.get('last_name')):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    form = '''
        <form method="get">
            <label for="fname">First name:</label>
            <input type="text" id="fname" name="first_name"><br><br>
            <label for="lname">Last name:</label>
            <input type="text" id="lname" name="last_name"><br><br><br>
            <input type="submit" value="Submit"><br>
        </form> 
    '''

    string = form + format_list_teachers(teachers)
    response = HttpResponse(string)
    return response


def create_teacher_view(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = F'''
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Submit"><br>
            </form> 
        '''
    return HttpResponse(html_form)


def update_teacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html_form = F'''
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Submit"><br>
                <a href="/teachers/">Back to list</a>
            </form> 
        '''
    return HttpResponse(html_form)