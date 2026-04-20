from django.contrib import admin
from django.urls import include, path

from users.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', HomeView.as_view(), name='home'),
]
