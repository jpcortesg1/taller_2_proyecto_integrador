from django.contrib import admin
from django.urls import path
from petclassiffier import views as petclassiffier_views

from django.conf import settings
from django.conf.urls.static import static

import petclassiffier

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', petclassiffier_views.home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
