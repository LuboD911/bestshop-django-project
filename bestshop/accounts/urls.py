from django.urls import path

from bestshop.accounts.views import login_user, logout_user, register_user, profile_details

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', register_user, name='register user'),
    path('profile/', profile_details, name='profile details'),

)