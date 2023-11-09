from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("all/", views.leads, name="all_leads"),
    path("add/", views.add_lead, name="add_leads"),
    path("<pk>/", views.leads_detail, name="details"),
]
