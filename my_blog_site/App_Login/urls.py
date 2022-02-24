from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('profile/',views.profile,name = 'profile'),
    path('changeUserInfo/',views.changeUserInfo,name='changeUserInfo'),
    path('password/',views.changePassword,name='password'),
    path('change_profile/',views.change_profile,name = 'change_profile'),
    path('update_profile_pic/',views.update_profile_pic,name= 'update_profile_pic')





]