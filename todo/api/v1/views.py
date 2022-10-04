from .serializers import TaskSerializer
from rest_framework import filters 
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from todo.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('title',)
    ordering_fields = ['created_date', 'done']

    def get_queryset(self):
        """
            Getting user for not having access to the rest of the Task.
        """
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)