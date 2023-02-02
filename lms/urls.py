from django.contrib import admin
from django.urls import path, include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),

    path('students/', include('students.urls')),

    path('teachers/', include('Teachers.urls')),

    path('groups/', include('groups.urls')),

]
