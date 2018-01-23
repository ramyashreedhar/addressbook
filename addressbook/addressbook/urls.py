"""addressbook URL Configuration

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
from django.urls import path
from  django.contrib.auth import views

from contacts import views as contviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),

    path('', contviews.ListContactView.as_view(),
        name='contacts-list',),
    path('<int:pk>/', contviews.ContactView.as_view(),
        name='contacts-view',),
    path('new', contviews.CreateContactView.as_view(),
        name='contacts-new',),
    path('edit/<int:pk>/', contviews.UpdateContactView.as_view(),
        name='contacts-edit',),
    path('edit/<int:pk>/addresses', contviews.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
    path('delete/<int:pk>/', contviews.DeleteContactView.as_view(),
        name='contacts-delete',),

]

