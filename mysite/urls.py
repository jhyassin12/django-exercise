from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("program.urls")),
    path('program/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('program/',include('django.contrib.auth.urls'))
]