from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Student


def index(request):
    students = Student.objects.all().order_by('birthday')
    # string = '<br>'.join(str(student) for student in students)
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthday</th></tr><thead><tbody>'
    for st in students:
        string += f'<fr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td></tr>'
    string += '</tbody></table>'
    response = HttpResponse(string)
    return response



