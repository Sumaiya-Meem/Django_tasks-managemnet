
from django.contrib import admin
from django.urls import path,include
# from tasks.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls")),
]
