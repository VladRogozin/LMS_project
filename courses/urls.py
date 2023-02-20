
from django.urls import path

from courses.views import get_courses
from courses.views import create_course_view
from courses.views import UpdateCourseView
from courses.views import detail_course
from courses.views import delete_course

app_name = 'courses'

urlpatterns = [
    path('', get_courses, name='list'),
    path('create/', create_course_view, name='create'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_course, name='detail'),
    path('delete/<int:pk>/', delete_course, name='delete'),
]