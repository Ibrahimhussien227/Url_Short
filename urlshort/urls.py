from django.contrib import admin
from django.urls import path, include
from root.views import sayHello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('root.urls'))
]
