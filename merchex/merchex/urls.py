"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.about),
    path('',views.bands_listing,name='band-list'),
    path('contact-us/',views.Contact,name="contact"),
    path('bands/<int:id>/',views.band_detail,name='band-detail'),
    path('listings/',views.listings,name='listings'),
    path('listings/<int:id>/', views.listings_detail, name='listings-detail'),
    path('email-sent/', views.email, name='email-sent'),
    path('bands/add/', views.band_create, name='band-create'),
    path('listings/add/', views.listing_create, name='listing-create'),




]
