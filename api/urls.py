from django.urls import path
from . import views


urlpatterns = [
    path('category/create/list/', views.CategoryListCreateView.as_view()),
    path('category/detail/<int:id>/', views.ProductDetailView.as_view()),
    path('product/create/list/', views.ProductListCreateView.as_view()),
    path('product/detail/<int:id>/', views.ProductDetailView.as_view()),
    path('log-in', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/delete/<int:pk>/', views.product_delete),
    path('add-to-cart/<int:product_id>/', views.AddToCartView.as_view()),
    # =================================================================================================
    path('banner/create/list/', views.BannerListCreateView.as_view()),
    path('banner/detail/<int:pk>/', views.BannerRetrieveUpdateDestroyView.as_view()),
    path('info/create/list/', views.InfoListCreateView.as_view()),
    path('info/detail/<int:pk>/', views.InfoRetrieveUpdateDestroyView.as_view()),
    path('product_enter/create/list/', views.ProductEnterListCreateView.as_view()),
    path('product_enter/detail/<int:pk>/', views.ProductEnterRetrieveUpdateDestroyView.as_view()),
    path('wishlist/create/list/', views.WishlistListCreateView.as_view()),
    path('wishlist/detail/<int:pk>/', views.WishlistRetrieveUpdateDestroyView.as_view()),
]