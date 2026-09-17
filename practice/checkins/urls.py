from django.urls import path

from checkins.views import home, get_form, report , about

app_name = 'checkins'

urlpatterns = [
    path('', home , name='home'),
    path('home/' , home , name = 'home'),
    path('add/', get_form, name='add'),
    path('report/', report , name = 'report'),
    path('about/' , about , name='about')
]
