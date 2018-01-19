"""invite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from users.views import signup, UserInviteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/', LogoutView.as_view(), name='logout'),
    url(r'^accounts/register/', signup, name='register'),
    url(r'^$', UserInviteView.as_view(), name="home"),
    url(r'^invite/(?P<invite_data>\w+)', signup, name="invite"),
]
