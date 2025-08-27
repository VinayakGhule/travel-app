from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
#    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    path('',include('bookings.urls')),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('logout/',views.logout_view, name='logout'),
    path('forbidden/',views.forbidden_view, name='forbidden'),
]