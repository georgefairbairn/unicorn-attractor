"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from accounts import urls as urls_accounts
from tickets import urls as urls_tickets
from blog import urls as urls_blog
from stats import urls as urls_stats
from tickets.views import all_tickets
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='tickets/')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^blog/', include(urls_blog)),
    url(r'^stats/', include(urls_stats)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
