from django.urls import path

from .views import HomeView, ElementosView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('elementos/', ElementosView.as_view(), name='home'),
]
