"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

picture_url = "https://picsum.photos/id/247/720/405"


def get_picture(request):
    print(picture_url)
    return JsonResponse({"picture_url": picture_url})


def set_picture(request):
    if request.method == "POST":
        global picture_url
        picture_url = json.loads(request.body)["picture_url"]
        picture_url = picture_url
        return JsonResponse({"picture_url": picture_url})
    
@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"success": True})


urlpatterns = [
    path("get-picture", get_picture),
    path("set-picture", set_picture),
    path("get-csrf-token", get_csrf_token),
]
