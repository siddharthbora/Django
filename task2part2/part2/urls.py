from django.urls import path
from . import views


urlpatterns=[
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('success/',views.success,name='success'),
    path('logout/',views.userlogout,name='logout')
]