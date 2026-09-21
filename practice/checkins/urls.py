from django.urls import path

from checkins.views import about, get_form, home, report

app_name = "checkins"

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("add/", get_form, name="add"),
    path("report/", report, name="report"),
    path("about/", about, name="about"),
]
