from django.urls import path

from api.views.kit import KitView
from .views.users import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('my-kit/', KitView.as_view(), name='my-kit')
    # GET for landing screen (image/text previews), from there, can POST
        # POST:
            # possibly drop-down with Image and Text as options; choosing one will redirect to form
            # or could have + button at top right of divs to add image / text
    # GET by ID for individual images or text pieces (you access by clicking from landing), would have separate route, will have additional info (from there, can PUT, DEL)
]