from datetime import datetime
from django_filters import rest_framework as filters
  
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer, FilterSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    
    '''
    
        + GET /drivers/driver/ - вивід списку водіїв
        + GET /drivers/driver/?created_at__gte=10-11-2021 - вивід списку водіїв, які створені після 10-11-2021
        + GET /drivers/driver/?created_at__lte=16-11-2021 - вивід списку водіїв, котрі створені до 16-11-2021

        + GET /drivers/driver/<driver_id>/ - отримання інформації по певному водію
        + POST /drivers/driver/ - створення нового водія
        + UPDATE /drivers/driver/<driver_id>/ - редагування водія
        + DELETE /drivers/driver/<driver_id>/ - видалення водія

        Vehicle:
        + GET /vehicles/vehicle/ - вивід списку машин
        + GET /vehicles/vehicle/?with_drivers=yes - вивід списку машин з водіями
        + GET /vehicles/vehicle/?with_drivers=no - вивід списку машин без водіїв

        + GET /vehicles/vehicle/<vehicle_id> - отримання інформації по певній машині
        + POST /vehicles/vehicle/ - створення нової машини
        + UPDATE /vehicles/vehicle/<vehicle_id>/ - редагування машини
        + POST /vehicles/set_driver/<vehicle_id>/ - садимо водія в машину / висаджуємо водія з машини  
        + DELETE /vehicles/vehicle/<vehicle_id>/ - видалення машини

    '''
    api_urls ={
        'Driver list':'/drivers/driver/',
        'Driver info':'/drivers/driver/<str:pk>/',
        'Delete driver':'/drivers/driver/<str:pk>/',
        'Vehicle list':'/vehicles/vehicle/',
    }
    return Response(api_urls) 

class DrvFilter(filters.FilterSet):
    created_at__gte = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_at__lte = filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Driver
        fields = { 'created_at': ['gte','lte'],}


class DriversList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = DriverSerializer
    filterset_class = DrvFilter

    # @api_view(['GET','POST'])
    def get_queryset(self):
        '''Allow us to create a driver and get drivers list'''

        if self.request.method == 'GET': #list
            drivers = Driver.objects.all() 
            serializer = DriverSerializer(drivers, many=True)
            return  drivers

        elif self.request.method == 'POST':  #create
            serializer = DriverSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
            return serializer.data

    # def get_queryset(self):
    #     """
    #     Optionally res
    #     """
    #     queryset = Driver.objects.all()
    #     # filter_prop = self.request.query_params.get('created_at__gte')
    #     filter_prop = self.request.query_params.get('created_at__gte')
    #     print("LALALALLALA",filter_prop)
        

    #     if filter_prop is not None:
    #         urllDate = datetime.strptime(filter_prop, '%d-%m-%Y')
    #         urllDate = urllDate.date()
    #         # drivers = drivers.filter(created_at = urllDate)
    #         drivers = queryset.filter(created_at__gte = urllDate)
    #     return drivers
        
        # elif filter_prop is not None:
        #     # drivers = drivers.filter(created_at = urllDate)
        #     drivers = self.drivers.filter(created_at__gte = urllDate)
        #     return drivers    





    # param = request.GET.get('created_at__gte',none)
    # if param:
    #     drivers = Driver.objects.all()
    #     serializer = DriverSerializer(drivers, many=True)
    #     f = StartFilter(request.GET, drivers)
    #     render(request, 'my_app/template.html', {'filter': f})


@api_view(['POST','GET','DELETE'])
def driverUpDelDet(request, pk): 
    '''Allows update/delete and show detail'''
    if request.method == 'GET': # driver detail
        driver = Driver.objects.get(id=pk) 
        serializer = DriverSerializer(driver, many=False)
        return Response(serializer.data)

    elif request.method == 'POST': # update
        driver = Driver.objects.get(id=pk)
        serializer = DriverSerializer(instance=driver,  data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE': # delete
        driver = Driver.objects.get(id=pk) 
        driver.delete()
        return Response("Succsesfully deleted")

# Vehicle views
@api_view(['GET','POST'])
def vehicleTool(request): 
    '''Allow us to create vehicle and get vehicles list'''
    
    if request.method == 'GET': #list
        vehicles = Vehicle.objects.all() 
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':  #create
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['POST','GET','DELETE'])
def vehicleUpDelDet(request, pk):
    '''Allows update/delete and show detail'''
    
    if request.method == 'GET': # vehicle detail
        vehicle = Vehicle.objects.get(id=pk) 
        serializer = VehicleSerializer(vehicle, many=False)
        return Response(serializer.data)

    elif request.method == 'POST': # update
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle,  data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE': # delete
        vehicle = Vehicle.objects.get(id=pk) 
        vehicle.delete()
        return Response("Vehicle is succsesfully deleted")













