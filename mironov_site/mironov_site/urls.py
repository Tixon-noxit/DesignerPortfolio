from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from main.views import MironovProject, MironovCreation, index, MironovAbout, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='OFFMAXLINE'),
    re_path(r'^projects/$', MironovProject.as_view(), name='Projects'),
    re_path(r'^creation/$', MironovCreation.as_view(), name='Creation'),
    re_path(r'^about/$', MironovAbout.as_view(), name='About'),
    # path('about/', include('about.urls')),
    # path('test_contacts/', include('about.urls')),
    
    re_path(r'^contacts/$', contacts, name='Contacts'),
    
]


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

