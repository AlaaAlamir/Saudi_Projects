"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from home import views as h
from neom import views as n
from worldcup import views as w
from expo import views as e

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',h.landpage,name='landpage'),
    path('vision2030/',h.vision2030,name='vision2030'),
    path('/create/',h.create,name='create'),
    path('vision2030/delete/<int:id>/',h.delete,name='delete'),
    path('edit/<int:id>/',h.edit,name='edit'),
    path('update/',h.update,name='update'),
    path('neom/',n.neom,name='neom'),
    path('worldcup2034/',w.saudi2034,name='saudi2034'),
    path('expo/',e.expo,name='expo'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
