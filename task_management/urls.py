
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
# from tasks.views import
from debug_toolbar.toolbar import debug_toolbar_urls

def home_view(request):
    return HttpResponse("Welcome to Task Management!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tasks/", include("tasks.urls")),
     path('', home_view, name='home'),
]+ debug_toolbar_urls()
