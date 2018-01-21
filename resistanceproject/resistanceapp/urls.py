from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('', views.SoldierListView.as_view(), name='dashboard-soldiers'),
    path('new', views.SoldierCreateView.as_view(), name='soldier-new'),
    path('<pk>/', views.SoldierDetailView.as_view(), name='soldier-detail'),
    path('<pk>/update', views.SoldierUpdateView.as_view(), name='soldier-update'),
    path('<pk>/delete', views.SoldierDeleteView.as_view(), name='soldier-delete'),
    path('<pk>/dieonthefield', views.SoldierDeadOnTheField.as_view(), name='soldier-die'),
]
