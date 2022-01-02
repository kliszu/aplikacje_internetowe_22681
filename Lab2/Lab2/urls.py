from django.urls import path, include
from django.contrib import admin

import account.views

urlpatterns = [
    path('privacy/', account.views.privacy),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/',
        include('social_django.urls', namespace='social')),
]