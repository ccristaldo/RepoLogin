from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
	
	path('login/', views.Login, name='login'),
	]
	
