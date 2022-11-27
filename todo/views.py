from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Task
from .tasks import task_delete

# Create your views here.


class IndexView(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ("title",)
    success_url = reverse_lazy("todo:index")

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class TaskDoneView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = True
        object.save()
        return redirect(self.success_url)


class TaskUndoneView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:index")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = False
        object.save()
        return redirect(self.success_url)


def taskdelete(self, request):
    task_delete.delay()
    return taskdelete