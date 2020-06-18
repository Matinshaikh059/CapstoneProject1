from django.urls import path
from . import views
urlpatterns = [
    # path("customer_page", views.customer_home),
    path('send_account', views.send_account),
    path('get_new_account', views.new_account),
    path('applypassbook', views.applypassbook),
    path('applychequebook', views.applychequebook),
]