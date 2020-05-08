from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

# Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.