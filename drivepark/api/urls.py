from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
  #drivers
    path('drivers/driver/', views.DriversList.as_view(), name='drivers-tool'),
    path('drivers/driver/<str:pk>', views.driverUpDelDet, name='driver-UpdateDeleteDetail'),
  #vehicles
    path('vehicles/vehicle/', views.vehicleTool, name='vehicle-list'),
    path('vehicles/vehicle/<str:pk>', views.vehicleUpDelDet, name='vehicle-UpdateDeleteDetail'),
 
]