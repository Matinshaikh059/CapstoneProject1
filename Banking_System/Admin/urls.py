from django.urls import path
from . import views
urlpatterns = [
    # path("admin_page", views.admin_home),
    path("add_employee", views.add_employee),
    path("remove_employee", views.remove_employee),
    path("search_customer", views.search_customer),
    path("search_employee", views.search_employee),
    path("set_transaction_limit", views.set_transaction_limit),
    path("update_emp_details", views.update_employee_details),
]
