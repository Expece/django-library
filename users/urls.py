from django.urls import path, include
from .views import PersonalAccount, SignUpUser, SignIpUser, signOutUser


urlpatterns = [
    path('', PersonalAccount.as_view(), name='personal_account'),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('signin/', SignIpUser.as_view(), name='signin'),
    path('signout/', signOutUser, name='signout'),
]