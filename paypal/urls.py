from argparse import Namespace
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from . import views 
from Menus.views import sitemap
from pages.views import view_page

urlpatterns = [
    path('', views.hola, name='inicio' ),
    
]