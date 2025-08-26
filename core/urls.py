from django.urls import path
from . import views
from . import contact_views

urlpatterns = [
    path('', views.index, name='index'),
    path('service-details/', views.service_details, name='service-details'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/submit/', contact_views.contact_form_handler, name='contact_form_handler'),
]
