"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from models_api.views import MyModelView, MyModelDetails, ObtainToken
from mu_models.views import MyModelView2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/', MyModelView.as_view(), name='model-list'),
    path('models/<int:pk>', MyModelDetails.as_view(), name='model-list-details'),
    path('a/', MyModelView2.as_view(), name='a-list'),
    path('token/', ObtainToken.as_view(), name='token')
]
