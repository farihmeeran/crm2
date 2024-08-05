from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.home,name = ""),

    path('register',views.register, name = "register"),

    path('my-login',views.my_login, name = "my-login"),

    path('user-logout',views.user_logout, name = "user-logout"),


    # - CRUD

    path('dashboard',views.dashboard, name = "dashboard"),

    path('create-record',views.add_customer, name = "create-record"),

    path('update-record/<int:pk>',views.update_customer, name = "update-record" ),

    path('record/<int:pk>',views.single_customer, name = "record"),

    path('delete-record/<int:pk>',views.delete_customer, name = "delete-record"),
]

