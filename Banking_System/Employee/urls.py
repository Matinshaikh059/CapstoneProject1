from django.urls import path
from . import views
urlpatterns = [
    # path("employee_page", views.employee_home),
    path("add_customer", views.add_customer),
    path("remove_account", views.remove_account),
    path("add_account", views.add_account),
    path("update_cust_details", views.update_cust_details),
    path("emp_search_customer", views.emp_search_customer),
]
