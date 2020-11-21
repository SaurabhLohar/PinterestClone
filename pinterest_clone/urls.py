"""pinterest_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views as user_views
from django.contrib.auth import views as auth_views




urlpatterns = [ 
	path('pinterest/admin/', admin.site.urls),

	path('',include('pinterest.urls')),

	path('register/', user_views.register, name="register"),

    path('login/', user_views.userlogin, name="login"), 

    path('logout/',user_views.userLogout,name="logout"),

    path('account/info/',user_views.userInfo,name="account-setting"),

# change password
   
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='account/password.html'),name='password_change'),

    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='account/password-changed.html'),name='password_change_done'),

# reset password urls
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='account/reset.html'),name='reset_password'),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/reset_form.html'),name='password_reset_confirm'),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# ---------------------------------------------------------------------
# handling url errors
    handler404 = 'pinterest.views.handler404'
    handler500 = 'pinterest.views.handler500'
