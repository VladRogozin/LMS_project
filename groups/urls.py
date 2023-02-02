
from django.urls import path

from groups.views import get_groups
from groups.views import create_group_view
from groups.views import update_group
from groups.views import detail_group
from groups.views import delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group_view, name='create'),
    path('update/<int:pk>/', update_group, name='update'),
    path('detail/<int:pk>/', detail_group, name='detail'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]