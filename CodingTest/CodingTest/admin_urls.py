from django.contrib import admin
from django.urls import path


# Admin Urls
urlpatterns = [
    path('', admin.site.urls),
]