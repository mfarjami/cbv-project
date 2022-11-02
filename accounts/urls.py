<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
>>>>>>> pytest
from . import views

app_name = "accounts"

urlpatterns = [
<<<<<<< HEAD
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('api/v1/', include('accounts.api.v1.urls')),

]
=======
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
>>>>>>> pytest
