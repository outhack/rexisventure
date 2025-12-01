from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("capabilities/", views.capabilities, name="capabilities"),
    path("industries/", views.industries, name="industries"),
    path("government/", views.government, name="government"),
    path("partners/", views.partners, name="partners"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

