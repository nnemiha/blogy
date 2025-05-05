# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include

# Добавьте эти два импорта:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Сначала свои кастомные views (signup и т.п.)
    path('accounts/', include('accounts.urls')),
    # Потом стандартные auth
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('blog.urls')),
]

# Только при DEBUG=TRUE: отдать статику из STATIC_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

