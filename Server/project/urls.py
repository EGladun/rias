"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from pdfconverter import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from pdfconverter.views import FileView, FileUpload

router = routers.DefaultRouter()
router.register('groups', views.GroupViewSet)
router.register('users/register', views.CreateUserView)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', obtain_auth_token, name='api_token_auth'),
    url(r'^upload/$', FileView.as_view()),
    url(r'^result/$', FileUpload.as_view({'get': 'list'}))

]
