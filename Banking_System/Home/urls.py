from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('admin_page', views.direct),
    path('employee_page', views.direct2),
    path('customer_page', views.direct3),
    
]
