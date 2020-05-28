
from django.urls import path
from . import view

urlpatterns = [
  path("eggs/",view. eggs), #For writing anything
    path('', view. homepage, name = "home"),
   path("count/", view. count, name = "counting"),
    path("About/",view.AboutPage, name = "about")

]
