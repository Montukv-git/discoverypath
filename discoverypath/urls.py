from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name='signup'),
    path('test/', views.test, name='test'),
    path('results/', views.results, name='results'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]