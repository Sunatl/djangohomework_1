from django.urls import path
from .views import *

urlpatterns = [
    path("",get_all_carr,name="get_aal"),
    path("get_all",get_all,name="get_all"),
    path("get_by_id/<int:pk>",get_by_id,name="Get_by_id"),
    path("add",add,name="add"),
    path("update/<int:pk>",update,name="update"),
    path("delete/<int:pk>",delete,name="delete"),
    path("get_company",get_company,name="get_company"),
    path("get_by_company/<int:pk>",get_by_company,name="Get_by_id"),
    path("add_company",add_company,name="add_company"),
    path("update_company/<int:pk>",update_company,name="update_company"),
    path("delete_company/<int:pk>",delete_company,name="delete_company")
    
]