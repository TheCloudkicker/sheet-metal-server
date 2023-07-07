from django.urls import path, include, re_path
from .api.purchase_orders import PurchaseOrdersDetailAPI, PurchaseOrdersListAPI
from .api.jobs import JobsDetailAPI, JobsListAPI
from .api.customers import CustomersDetailAPI, CustomersListAPI


app_name = "main"

from .api import *


urlpatterns = [
    path("customers/", CustomersListAPI.as_view()),
    path("customers/<pk>", CustomersDetailAPI.as_view()),
    path("jobs/", JobsListAPI.as_view()),
    path("jobs/<pk>", JobsDetailAPI.as_view()),
    path("purchase-orders/", PurchaseOrdersListAPI.as_view()),
    path("purchase-orders/<pk>", PurchaseOrdersDetailAPI.as_view()),
]
