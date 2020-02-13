from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .router import router

urlpatterns = [
    path(r'', RedirectView.as_view(url='/book/bookshelf/')),
    path('book/', include('book_management.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
