from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview_links),
    path('task-list/', views.get_task_list),
    path('task-detail/<int:pk>/',views.task_detail),
    path('task-edit/<int:pk>/',views.task_edit),
    path('task-create/', views.task_create),
    path('task-delete/<int:pk>/', views.task_delete),

]