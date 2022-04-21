from django.urls import path

from api.views.kit import KitView, TextView
from .views.users import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('my-kit/', KitView.as_view(), name='my-kit'),
    path('my-kit/text/<int:pk>/', TextView.as_view(), name='my-kit'),
    # path('my-kit/Image/<int:pk>/', ImageView.as_view(), name='my-kit'),
]