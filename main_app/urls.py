from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wishitems/', views.wishitems_index, name='index'),
  path('wishitems/', views.WishitemList.as_view(), name='wishitems_index'),
  path('wishitems/create/', views.WishitemCreate.as_view(), name='wishitems_create'),
  path('wishitems/<int:pk>/delete/', views.WishitemDelete.as_view(), name='wishitems_delete'),
]