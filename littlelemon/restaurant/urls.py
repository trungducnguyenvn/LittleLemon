from . import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    path('', views.index, name='index'),
    path('menu-item', views.menu_item, name='menu-item'),
    path('menu', views.MenuItemView.as_view(), name='Menu-item'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view(), name='Single-Menu-Item'),
    path('message/', views.secret_view, name='message'),
    path('api-token-auth/', obtain_auth_token)
]