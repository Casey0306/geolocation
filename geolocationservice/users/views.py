from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CreateTokenSerializer, GetTokenSerializer
from .models import User
from companies.models import Company
from .const import FERNET_KEY
from cryptography.fernet import Fernet


class CreateTokenView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CreateTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mail = serializer.data['email']
        user = User.objects.filter(email=mail).first()
        fernet = Fernet(FERNET_KEY.encode('utf-8'))
        temp_token = serializer.data['token']
        cry_serializer_token = fernet.encrypt(temp_token.encode('utf-8'))
        if Company.objects.filter(user=user).update(
                company_token=cry_serializer_token.decode('utf-8')):
            comp = Company.objects.filter(user=user).first()
            comp.save()
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'token': serializer.data['token'],
                }
            status_code = status.HTTP_200_OK
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Authorization fails, check company and username',
            }

        return Response(response, status=status_code)


class GetTokenView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = GetTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        fernet = Fernet(FERNET_KEY.encode('utf-8'))
        temp_token = serializer.data['token'].encode('utf-8')
        decry_serializer_token = fernet.decrypt(temp_token).decode('utf-8')
        response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'token': decry_serializer_token,
                }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
