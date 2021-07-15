from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "homepage"
urlpatterns = [
    path('', views.home_view, name="home"),
    path('django/', views.django_view, name="django"),
    path('angular/', views.angular_view, name="angular"),
    path('asp/', views.asp_view, name="asp"),
    path('create/', views.createCourse_view, name="createCourse")

]

urlpatterns += staticfiles_urlpatterns()