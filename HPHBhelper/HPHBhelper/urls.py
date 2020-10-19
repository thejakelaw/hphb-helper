from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('albus/', admin.site.urls),
    path('hogwarts/', include('hogwarts.urls')),
]
