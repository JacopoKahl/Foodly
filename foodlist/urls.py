from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework import routers
from .views import FoodViewset, UserViewset
from django.conf import settings
from django.conf.urls.static import static

# Create router for REST API
router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('foodsapi', FoodViewset)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^features/$', views.features, name='features'),
    url(r'^recipes/$', views.recipes, name='recipes'),

    #User administration panels
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^panel/list/$', views.food_list, name='food_list'),
    url(r'^panel/list/del/(?P<pk>\d+)$', views.food_delete, name='food_delete'),
    url(r'^panel/list/add/$', views.food_add, name='food_add'),

    path('', include(router.urls))
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)