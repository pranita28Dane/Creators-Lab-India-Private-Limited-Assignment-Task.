from django.contrib.auth import views as auth_views
from django.urls import path
from myapp.views import register, custom_login, custom_logout, home, simple_upload, model_form_upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('simple/', simple_upload, name='simple_upload'),
    path('form/', model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)