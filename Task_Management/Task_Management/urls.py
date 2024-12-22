from django.contrib import admin
from django.urls import path
from Main_files import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Home, name='home'),
    path("task/", views.Tasks, name='task'),
    path("add_task/", views.add_task, name='add_task'),
    path("task_detail/", views.Task_details, name='task_details'),
    path("edit_task/<int:id>/", views.edit_task, name='edit_task'),  # Edit task URL
    path("delete_task/<int:id>/", views.delete_task, name='delete_task')  # Delete task URL
]
