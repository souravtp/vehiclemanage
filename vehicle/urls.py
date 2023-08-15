from django.urls import path

from . import views

urlpatterns = [
    path('create-vehicle/', views.VehicleCreateView.as_view()),
    path('list-vehicle/', views.VehicleListView.as_view()),
    path('vehicle-detail/<int:pk>/', views.VehicleDetailView.as_view()),
    path('update-vehicle/<int:pk>/', views.VehicleUpdateView.as_view()),
    path('delete-vehicle/<int:pk>/', views.VehicleDeleteView.as_view())
]
