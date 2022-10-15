
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Todo Api",
      default_version='v1',
      description="That's all the Api on the website.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="biroghlan95@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-docs/', include_docs_urls(title='api-docs')),
    path('swagger/todo-api.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
