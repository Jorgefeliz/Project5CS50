from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("event", views.event, name="event"),
    path("event/<int:event_id>/<str:status>", views.event_update, name="event_update"),
    path("announcement", views.announcement, name="announce"),
    path("announcement_update", views.announcement_update, name="announce_update"),
    path("announcement_retrieve", views.announcement_retrieve, name="announce_retrieve"),

]