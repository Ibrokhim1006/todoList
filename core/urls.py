from django.contrib import admin
from django.urls import path

from todo.views import todo_list,delet_doto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_list,name='todo_list'),
    path('<int:pk>/delete/',delet_doto)
]
