from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from companies.models import Company
from .serializers import RegistrationDeviceSerializer, SaveDeviceDataSerializer
from devices.models import Device
from .models import Location


class RegisterDeviceView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RegistrationDeviceSerializer
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'Device registered successfully',
        }

        return Response(response, status=status_code)


class SaveDeviceDataView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaveDeviceDataSerializer
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'Location saved successfully',
        }

        return Response(response, status=status_code)


class GetLastDeviceDataView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def post(self, request):
        try:
            company = Company.objects.get(user=request.user)
            device_id = request.data.get('device_id', None)
            device = Device.objects.filter(deviceid=device_id).first()
            location = Location.objects.filter(device=device).last()
            status_code = status.HTTP_200_OK
            if device:
                if device.company == company:
                    response = {
                        'success': 'true',
                        'status code': status_code,
                        'message': 'Device last location fetched successfully',
                        'data': [{
                            'latitude': location.latitude,
                            'longitude': location.longitude,
                            'company name': company.company_name,
                            'device id': device.deviceid,
                            'data': location.data
                                }]
                            }
                else:
                    raise NameError(
                        'This device id does not belongs to the auth Company!')
            else:
                raise NameError('This device id does not exists!')

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Auth fails, check token or deviceid parameter',
                'error': str(e)
                }
        return Response(response, status=status_code)
