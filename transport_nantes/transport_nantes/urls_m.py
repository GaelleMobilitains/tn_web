"""transport_nantes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from asso_tn.views import MainTransportNantes
from django.contrib.sites.models import Site

#print(Site.objects.get_current())
print('setting urlpatterns')

urlpatterns = [
    path('', MainTransportNantes.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('captcha/', include('captcha.urls')),
    path('tb/', include ('topicblog.urls')),
]
