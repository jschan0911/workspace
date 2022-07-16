"""church_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from work_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('list/', views.list, name='list'),
    path('list_create/', views.list_create, name='list_create'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
    path('age_up/', views.age_up, name='age_up'),
    path('age_down/', views.age_down, name='age_down'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('update_list/<int:list_id>', views.update_list, name='update_list'),
]
