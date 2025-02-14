"""
URL configuration for dominti_site_local project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Подключение маршрутов (URL-адресов) из приложения usersprojects к основному маршрутизатору Django
from django.urls import include

urlpatterns += [
    path('usersprojects/', include('usersprojects.urls')),
]

# Перенаправить корневой URl сайта на URL проекта urlsprojects:
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='usersprojects/', permanent=True))
]

# Использование функции static(), чтобы добавить сопоставление URL-адресов для обслуживания статических файлов только во время разработки