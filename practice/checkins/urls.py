from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from checkins.views import about, get_form, home, report

app_name = "checkins"

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("add/", get_form, name="add"),
    path("report/", report, name="report"),
    path("about/", about, name="about"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_URL)
