from django.contrib import admin
from django.urls import path
import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home, name="home"),
    path('result/', page.views.result, name="result"),
]
