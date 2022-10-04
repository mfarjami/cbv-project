from django.urls import path, include
from . import views



app_name = 'todo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/',views.TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/',views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',views.TaskDeleteView.as_view(), name='delete'),
    path('done/<int:pk>/',views.TaskDoneView.as_view(), name='done'),
    path('undone/<int:pk>/',views.TaskUndoneView.as_view(), name='undone'),
    path('api/v1/', include('todo.api.v1.urls')),
]

