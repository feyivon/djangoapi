from django.urls import path
from rest_framework.authtoken import views as auth_view
from . import views




urlpatterns=[
    path('user', auth_view.ObtainAuthToken.as_view(), name= 'login-user'),
    # path('users', views.UserRegisterEndpoint.as_view(), name='all_users'),
    path('categories', views.UpgradedCategoryEndpoint.as_view(), name='category'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category_single'),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name='category_delete'),
    path('products/', views.UpgradedProductEndpoint.as_view(), name='products'),
    # path('products/<int:pk>', views.ProductDetailEndpoint.as_view(), name='product_id'),
    path('products/<int:pk>', views.SingleProductEndpoint.as_view(), name='productss'),
    path('products_list', views.ProductListEndpoint.as_view(), name='products_list'),
    path('products/<int:product_id>/', views.ProductDetailEndpoint.as_view(), name='products'),

   
    

]
