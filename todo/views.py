from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
import requests, json
from .models import Task

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

@cache_page(60 * 20)
def weather(request):
    """
        It shows the weather condition of Tabriz city and updates every 20 minutes.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "80c8173748c3690246d4c2488e06feb7"
    city = "Tabriz"
    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url)
    return JsonResponse(response.json())