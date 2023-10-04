from rest_framework import generics
from .models import Material, Position, User, Brand, MaterialType, MaterialGroup, Currency, Client, Device,\
    Unit, Warehouse, Dealer
from .serializers import MaterialSerializer, PositionSerializer, UserSerializer, ClientSerializer, \
    CurrencySerializer, MaterialGroupSerializer, MaterialTypeSerializer, BrandSerializer, DealerSerializer, \
    DeviceSerializer, UnitSerializer, WarehouseSerializer


class PositionListAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class UserListApiView(generics.ListCreateAPIView):
    queryset = User
    serializer_class = UserSerializer


class MaterialGroupAPIView(generics.ListCreateAPIView):
    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupSerializer


class MaterialTypeAPIView(generics.ListCreateAPIView):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer


class WarehouseAPIView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class MaterialListAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class DeviceAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class ClientAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UnitAPIView(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class CurrencyAPIView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class DealerAPIView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class BrandAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
