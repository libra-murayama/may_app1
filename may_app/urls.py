
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),#追加
    path('accounts/', include('allauth.urls')),     #追加
]
