from django.urls import path
from . import views

app_name = 'estudios'
urlpatterns = [ 
       path('', views.DashboardView.as_view(), name='dashboard' ),
       path('home', views.HomeView.as_view(), name='home'),
]