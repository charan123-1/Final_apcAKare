from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('anantapur/', views.anantapur, name="anantapur"),
    path('guntur/', views.guntur, name="guntur"),
    path('chittoor/', views.chittoor, name="chittoor"),
    path('eastgodavari/', views.eastgodavari, name="eastgodavari"),
    path('kadapa/', views.kadapa, name="kadapa"),
    path('krishna/', views.krishna, name="krishna"),
    path('kurnool/', views.kurnool, name="kurnool"),
    path('prakasam/', views.prakasam, name="prakasam"),
    path('srikakulam/', views.srikakulam, name="srikakulam"),
    path('visakhapatnam/', views.visakhapatnam, name="visakhapatnam"),
    path('vizianagaram/', views.vizianagaram, name="vizianagaram"),
    path('westgodavari/', views.westgodavari, name="westgodavari")
]