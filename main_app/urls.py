from django.urls import path
from . import views
	
urlpatterns = [
	
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_grubbing/', views.add_grubbing, name='add_grubbing'),
    path('finches/<int:finch_id>/assoc_plaything/<int:plaything_id>/', views.assoc_plaything, name='assoc_plaything'),
    path('finches/<int:finch_id>/unassoc_plaything/<int:plaything_id>/', views.unassoc_plaything, name='unassoc_plaything'),

    path('playthings/', views.PlaythingList.as_view(), name='playthings_index'),
    path('playthings/<int:pk>/', views.PlaythingDetail.as_view(), name='playthings_detail'),
    path('playthings/create/', views.PlaythingCreate.as_view(), name='playthings_create'),
    path('playthings/<int:pk>/update/', views.PlaythingUpdate.as_view(), name='playthings_update'),
    path('playthings/<int:pk>/delete/', views.PlaythingDelete.as_view(), name='playthings_delete'),

 ]