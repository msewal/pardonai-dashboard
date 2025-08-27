from django.urls import path
from . import views

app_name = "charts"  

urlpatterns = [
    path('', views.dashboard, name='charts_home'),           
    path('plotly/', views.dashboard_plotly, name='plotly'),
]
