
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
# from tasks.views import
from debug_toolbar.toolbar import debug_toolbar_urls
from core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
    path('', home, name='home'),
]+ debug_toolbar_urls()
