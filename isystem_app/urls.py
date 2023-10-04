from django.urls import path
from .views import MaterialListAPIView, PositionListAPIView, UserListApiView, MaterialGroupAPIView, \
    MaterialTypeAPIView, WarehouseAPIView, DeviceAPIView, ClientAPIView, UnitAPIView, CurrencyAPIView, \
    DealerAPIView, BrandAPIView

app_name = 'system_app'

urlpatterns = [
    path('position/', PositionListAPIView.as_view(), name='position-list'),
    path('users/', UserListApiView.as_view(), name='user-list'),
    path('warehouse/', WarehouseAPIView.as_view(), name='warehouse-list'),
    path('materials-group/', MaterialGroupAPIView.as_view(), name='material-group-list'),
    path('materials-type/', MaterialTypeAPIView.as_view(), name='materials-type-list'),
    path('materials/', MaterialListAPIView.as_view(), name='material-list'),
    path('devices/', DeviceAPIView.as_view(), name='device-list'),
    path('units/', UnitAPIView.as_view(), name='unit-list'),
    path('currency/', CurrencyAPIView.as_view(), name='currency-list'),
    path('clients/', ClientAPIView.as_view(), name='material-list'),
    path('dealers/', DealerAPIView.as_view(), name='dealer-list'),
    path('brands/', BrandAPIView.as_view(), name='brand-list'),

]

