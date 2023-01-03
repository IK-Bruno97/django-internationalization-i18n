from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('', include('index.urls')),
    path('set_language/', set_language, name='set_language')
]
