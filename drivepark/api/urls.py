from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
  #drivers
    path('drivers/driver/', views.driverTool, name='drivers-tool'),
    path('drivers/driver/<str:pk>', views.driverUpDelDet, name='driver-UpdateDeleteDetail'),
  #vehicles
    path('vehicles/vehicle/', views.vehicleTool, name='vehicle-list'),
    path('vehicles/vehicle/<str:pk>', views.vehicleUpDelDet, name='vehicle-UpdateDeleteDetail'),
 
    path('drivers/drive/', views.DriversList.as_view(), name='test-filter'),
    # path('test/', views.fdriver_list, name='test'),
   # path('test/',views.get_queryset , name='test-filter'),
]
