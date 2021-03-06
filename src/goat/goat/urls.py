"""goat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from main.views import *

from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'api/characters', CharacterListView, base_name='character')
router.register(r'api/users', UserListView)
router.register(r'api/images', ImagesListView)
router.register(r'api/user', UserView, base_name='user')
router.register(r'api/raids', RaidsListView, base_name='raids')
router.register(r'api/bosses', BossListView, base_name='bosses')
router.register(r'api/articles', ArticlesListView)
router.register(r'api/current-articles', CurrentArticlesListView, base_name='current-articles')
router.register(r'api/current-boss', CurrentBossListView, base_name='current-boss')
router.register(r'api/raidbosses/(?P<raidid>[0-9]+)', RaidbossListView, base_name='raidbosses')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', views.obtain_auth_token),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
