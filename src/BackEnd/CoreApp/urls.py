from django.contrib import admin
from django.urls import path, include
from Apps.CalculatorApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authApp/', include('Apps.AuthApp.urls')),
    path('api/combatApp/', include('Apps.CalculatorApp.urls')),  # Incluye las URLs de la aplicación spells
    path('api/characterApp/', include('Apps.Characters.urls')),

] 