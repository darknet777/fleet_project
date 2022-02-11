from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='rental-home'),
    path('pricing/', views.pricing, name='rental-pricing'),
    path('gallery/', views.gallery, name='rental-gallery'),
    path('about/', views.about, name='rental-about'),
    path('contact/', views.about, name='rental-contact'),
]