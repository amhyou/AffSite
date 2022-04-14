from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('<str:topic>/<str:idd>', article, name="article"),
    path('<str:topic>', topic, name="topic"),
    path('terms/', terms, name="terms"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('privacy/', privacy, name="privacy"),
    path('copyright/', copyright, name="copyright"),

]
