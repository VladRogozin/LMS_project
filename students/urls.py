
from django.urls import path

from students.views import get_students
from students.views import create_student_view
from students.views import update_student
from students.views import detail_student
from students.views import delete_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student_view, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
