from django.urls import path
from .api_views import *

urlpatterns = [
    path('api/v1/user/login/', api_user_login_view, name="api_user_login"),
    path('api/v1/user/register/', api_register_view, name="api_register"),
    path('api/v1/user/profile/update/', api_profile_update_view, name="api_profile_update"),
    path('api/v1/user/profile/get/', api_profile_update_view, name="api_profile_get")
]
