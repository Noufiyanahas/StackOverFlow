from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("signup",views.UserView,basename="Users")
urlpatterns =[

]+router.urls