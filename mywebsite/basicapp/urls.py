from django.urls import path
from basicapp import views

app_name = "basicapp"

urlpatterns = [
    path("",views.home.as_view(),name="home"),
    path("about/",views.about.as_view(),name="about"),
    path("projects/",views.projects.as_view(),name="projects"),
    path("portfolio/",views.portfolio.as_view(),name="portfolio"),
    path("contacts/",views.contacts.as_view(),name="contacts"),
]
