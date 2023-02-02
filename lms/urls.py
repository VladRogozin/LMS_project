from django.contrib import admin
from django.urls import path, include

from Teachers.views import get_teachers, create_teacher_view, update_teacher, detail_teacher
from groups.views import get_groups, create_group_view, update_group, detail_group
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),

    path('students/', include('students.urls')),

    path('teachers/', get_teachers,),
    path('teachers/create/', create_teacher_view),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/detail/<int:pk>/', detail_teacher),
    path('groups/', get_groups,),
    path('groups/create/', create_group_view),
    path('groups/update/<int:pk>/', update_group),
    path('groups/detail/<int:pk>/', detail_group),
]
