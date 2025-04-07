"""cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from cartapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('detail/<int:productid>/', views.detail),
    path('addtocart/<str:ctype>/', views.addtocart),
    path('addtocart/<str:ctype>/<int:productid>/', views.addtocart),
    path('cart/', views.cart),
    path('cartorder/', views.cartorder),
    path('cartok/', views.cartok),
    path('cartordercheck/', views.cartordercheck),

    path('view_history_temperature/',views.view_history_temperature),
    path('add_temperature/',views.add_temperature),
    path('show_temperature1/',views.show_temperature1),

     #web api
    path('add_temperature_api/',views.add_temperature_api),
     #ajax
    path('show_temperature_api/',views.show_temperature_api),
    path('show_temperature2/',views.show_temperature2),
    
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL , document_root=settings.STATICFILES_DIRS)
