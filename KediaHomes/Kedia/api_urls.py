from django.urls import path
from .api_views import *


urlpatterns = [
    path('api/v1/kedia/projects/<str:slug>/', api_projects_view, name="api_projects"),
    path('api/v1/kedia/projects/', api_projects_view, name="api_projects"),
    path('api/v1/kedia/map/', api_map_view, name="api_map"),
    path('api/v1/kedia/map/<str:plot_no>/', api_map_one_view, name="api_map_one"),
    path('api/v1/kedia/contact-us/', api_contact_us_view, name="api_contact_us"),
    path('api/v1/kedia/news-letter/', api_news_letter_view, name="api_news_letter"),
]
