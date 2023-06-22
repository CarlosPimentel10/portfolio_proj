from django.contrib import admin
from django.urls import path, include
from portfolio_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='index'),
    path('user/<int:pk>/profile/', views.profile, name='user_profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/signup/', views.signup, name='account_signup'), 
    path('accounts/map/', views.map_view, name='map'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
