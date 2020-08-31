from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/' , admin.site.urls),
    url(r'', include('recipes.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns (
    #url(r'' , include('foodlist.urls')),
    path('', include('foodlist.urls')),
    path('auth/', obtain_auth_token),
    path('tinymce/', include('tinymce.urls')),
    path('tagging_autocomplete_new/', include('tagging_autocomplete_new.urls')),

    #prefix_default_language=False,
)

#Added new setting to static and media forlders
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
