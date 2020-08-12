from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^admin/' , admin.site.urls),
    url(r'', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns (
    #url(r'' , include('foodlist.urls')),
    path('', include('foodlist.urls')),
    path('tinymce/', include('tinymce.urls')),
    
    #prefix_default_language=False,
)
