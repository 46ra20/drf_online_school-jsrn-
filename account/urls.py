from django.urls import path,include
from .views import UserRegistrationView,ActiveAccount,UserLoginView,LogoutView,GetUserDetails,ResetPassword
urlpatterns = [
    path('registration/',UserRegistrationView.as_view(),name='registration'),
    path('active/<uid64>/<token>/',ActiveAccount),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    # get user data
    path('user_details/<pk>/',GetUserDetails),
    path('reset_password/<email>/',ResetPassword),
]
