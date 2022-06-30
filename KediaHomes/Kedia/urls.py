from django.contrib import admin
from django.urls import path
from Kedia import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("privacy/", views.privacy, name='privacy'),
    path("terms-and-conditions/", views.terms_and_conditions, name='terms_and_conditions'),
    path("disclaimer/", views.disclaimer, name='disclaimer'),
    path("gallery/", views.gallery, name='gallery'),
    path("projects/<str:slug>/", views.projects_view, name='projects'),
    path("palm/", views.palm, name='Palm'),
    path("oxygen/", views.oxygen, name='Oxygen'),
    path("corridor/", views.corridor, name='corridor'),
    path("ganesh/", views.ganesh, name='Ganesh Vihar'),
    path("ganeshext/", views.ganeshext, name='Ganesh Vihar Extension'),
    path("corpclub/", views.corpclub, name='Corporate Club'),
    path("kingdom/", views.kingdom, name='Kingdom'),
    path("capital/", views.capital, name='Capital'),
    path("projects/", views.projects, name='projects'),
    path("news-letter/", views.news_letter, name='news-letter'),
    path("map/", views.map_page_view, name='map_page'),
    path("map/booking/", views.map_view, name='map'),
    path("map/booking/<int:id>", views.booking_view, name='booking'),
    path("api/map/get/<int:id>", views.get_map_one_view, name='get_map_one'),
    # payment
    path("payment_gateway/", views.payment_gateway, name='payment_gateway'),
    path("map/booking/success", views.success, name='success'),
    path("map/booking/failure", views.failure, name='failure'),
    # edits
    # path("test-rk", views.test_rk),
    # path("pricing-test", views.pricing_test),
    path("sold_out/", views.sold_out),
    path("blog/", views.blog, name="blog"),
    path("comingsoon/", views.comingsoon, name="comingsoon"),
    path("indextest/", views.indextest, name="indextest")

]



