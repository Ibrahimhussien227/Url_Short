from django.urls import path
from root.views import sayHello

urlpatterns = [
    path('',sayHello)
]
