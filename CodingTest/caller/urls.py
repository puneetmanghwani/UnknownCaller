from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from caller.views import MarkSpamView,SearchView,DetailView


urlpatterns = [
    # taking number in params of url.
    path('spam/<int:pk>/', MarkSpamView.as_view(), name='markspam'),
    path('search/', SearchView.as_view(), name='search'),
    path('number/', DetailView.as_view(), name='detail')
]
