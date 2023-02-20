
from django.urls import path

from Teachers.views import ListTeacherView
from Teachers.views import CreateTeacherView
from Teachers.views import UpdateTeacherView
from Teachers.views import DetailTeacherView
from Teachers.views import DeleteTeacherView

app_name = 'teachers'

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete'),
]