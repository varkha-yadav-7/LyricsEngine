from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('search/',views.search),
    path('lyrics/',views.lyrics),
    path('collections/',views.collections),
]