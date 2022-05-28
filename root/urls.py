from django.urls import path
from root.views import routeToURL, createUrl

urlpatterns = [
    path('', createUrl),
    path('<slug:key>/', routeToURL)
]
