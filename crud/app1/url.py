from . import views
from django.urls import path

urlpatterns = [
    path('taskapi',views.task.as_view(),name='task'),
    path('task/<int:pk>',views.taskid.as_view(),name='taskid'),
]