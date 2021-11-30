"""Gest_Qui URL Configuration

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('acceuil.urls')),
    path('A_propos',include('A_propos.urls')),
    path('clients',include('clients.urls')),
    path('commande',include('commande.urls')),
    path('connexion',include('connexion.urls')),
    path('contact',include('contact.urls')),
    path('pagnier', include('pagnier.urls')),
    path('produits', include('produits.urls')),
    path('service', include('service.urls')),
    path('formulaire', include('formulaire.urls')),

]
