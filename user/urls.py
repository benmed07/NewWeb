from django.urls import path

from user import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update', views.user_update, name='user_update'),
    path('password', views.user_password, name='user_password'),
    path('orders', views.user_orders, name='user_orders'),
    path('order_product', views.user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),
    path('comments', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
    path('releve', views.releve, name='releve'),
    path('profile_pro', views.profile_pro, name='profile_pro'),

]