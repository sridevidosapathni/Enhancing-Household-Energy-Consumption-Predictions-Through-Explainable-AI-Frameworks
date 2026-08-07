"""
URL configuration for mental_health_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from adminapp import views as admin_views
from userapp import views as user_views
from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    #admin views
    path('admin/', admin.site.urls),
    path('admin-dashboard',admin_views.admin_dashboard,name='admin_dashboard'),
    path('pending-users',admin_views.pending_users,name='pending_users'),
    path('all-users',admin_views.all_users,name='all_users'),
    path('graph/',admin_views.graph,name='graph'),
    path('accept-user/<int:id>', admin_views.accept_user, name = 'accept_user'),
    path('reject-user/<int:id>', admin_views.reject_user, name = 'reject'),
    path('delete-user/<int:id>', admin_views.delete_user, name = 'delete_user'),
    
   
    path('random', admin_views.random, name = 'random'),
    path('randomforest_btn', admin_views.randomforest_btn, name='randomforest_btn'),
    
    
    path('LGBMR', admin_views.LGBMR, name = 'LGBMR'),
    path('lgbmr_btn', admin_views.lgbmr_btn, name='lgbmr_btn'),
    
    path("admin-change-status/<int:id>",admin_views.Change_Status,name="change_status"),
    path("delete_user/<int:id>",admin_views.delete_User,name="delete_user"),
    path("adminrejectbtn/<int:x>",admin_views.Admin_Accept_Button,name="adminaccept"),
    path("adminacceptbtn/<int:x>",admin_views.Admin_Reject_Btn,name="adminreject"),
   



    
    #user views
   
    path('user-about',user_views.user_about,name='user_about'),
    path('user-admin',user_views.user_admin,name='user_admin'),
    path('user-contact',user_views.user_contact,name='user_contact'),
    path('user-dashboard',user_views.user_dashboard,name='user_dashboard'),
   
    path('',user_views.user_index,name='user_index'),
    path('user-login',user_views.user_login,name='user_login'),
    path('user-prediction',user_views.user_prediction,name='user_prediction'),
    
    path('register',user_views.register,name='user_register'),
    path('userlogout/', user_views.userlogout, name = 'userlogout'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
