from django.urls import path
from . import views
urlpatterns = {
    path("challengeshome", views.index),
    path("january", views.jan),
    path("february", views.feb),
    path("march", views.mar),
    path("april", views.apr),
    path("may", views.may),
    path("june", views.jun),
    path("july", views.jul),
    path("august", views.aug),
    path("september", views.sep),
    path("ocotober", views.oct),
    path("november", views.nov),
    path("december", views.dec)

}
