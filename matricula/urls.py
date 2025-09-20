"""
URL configuration for matricula project.

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
from aluno import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.index, name='index'),
    path('alunos/', views.alunos, name='alunos'),
    path('alunos/novo/', views.alunos_create, name='alunos_create'),
    path('alunos/<int:pk>/', views.alunos_detail, name='alunos_detail'),
    path('alunos/<int:pk>/editar/', views.alunos_update, name='alunos_update'),
    path('alunos/<int:pk>/deletar/', views.alunos_delete, name='alunos_delete'),
]
