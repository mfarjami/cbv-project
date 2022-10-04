
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-docs/', include_docs_urls(title='api-docs'))

]
