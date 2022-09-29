from django.urls import path
from .views import SignUpUser, SignInUser, signOutUser, UserProfile, UpdateUser


urlpatterns = [
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('signin/', SignInUser.as_view(), name='signin'),
    path('signout/', signOutUser, name='signout'),
    path('<int:user_pk>', UpdateUser.as_view(), name='updateuser'),
    path('<str:user_slug>/', UserProfile.as_view(), name='profile'),
]