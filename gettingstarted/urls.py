from django.urls import path, include

from django.contrib import admin

admin.autodiscover()
from django.conf.urls.static import static
import hello.views
from django.conf import settings

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.home, name="home"),
    path("admin/", admin.site.urls),
    path('anantapur/', hello.views.anantapur, name="anantapur"),
    path('guntur/', hello.views.guntur, name="guntur"),
    path('chittoor/', hello.views.chittoor, name="chittoor"),
    path('eastgodavari/', hello.views.eastgodavari, name="eastgodavari"),
    path('kadapa/', hello.views.kadapa, name="kadapa"),
    path('krishna/', hello.views.krishna, name="krishna"),
    path('nellore/', hello.views.nellore, name="nellore"),
    path('kurnool/', hello.views.kurnool, name="kurnool"),
    path('prakasam/', hello.views.prakasam, name="prakasam"),
    path('srikakulam/', hello.views.srikakulam, name="srikakulam"),
    path('visakhapatnam/', hello.views.visakhapatnam, name="visakhapatnam"),
    path('vizianagaram/', hello.views.vizianagaram, name="vizianagaram"),
    path('westgodavari/', hello.views.westgodavari, name="westgodavari")
]
