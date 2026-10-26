
from django.urls import path

from item_category.views import ProductCategoryListView,ProductCategoryCreateView
from item_category.views import ProductCategoryRetrieveView,ProductCategoryUpdateDeleteView

urlpatterns = [

    # route for listing product categories
    path("product/all/",ProductCategoryListView.as_view()),

    # route to create product categories
    path("product/add/",ProductCategoryCreateView.as_view()),

    # route to retrieve product categorie
    path("product/one/<int:pk>/",ProductCategoryRetrieveView.as_view()),

    # route to update,delete product categories
    path("product/<int:pk>/",ProductCategoryUpdateDeleteView.as_view()),
]