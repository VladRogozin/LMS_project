
from django.urls import path

from Teachers.views import get_teachers
from Teachers.views import create_teacher_view
from Teachers.views import update_teacher
from Teachers.views import detail_teacher
from Teachers.views import delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher_view, name='create'),
    path('update/<int:pk>/', update_teacher, name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]