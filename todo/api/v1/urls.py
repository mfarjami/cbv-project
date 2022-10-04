from rest_framework import routers
from . import views

app_name = 'api_v1'


router = routers.DefaultRouter()

router.register('task', views.TaskViewSet, basename='task')
urlpatterns = router.urls
