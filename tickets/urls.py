from django.urls import path
from . import views


app_name = "tickets"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:ticket_id>/", views.detail, name="detail"),
    path("new/", views.new, name="new"),
]
