from rest_framework import serializers
from companies.models import Company
from .models import Device, Location
from locationmap.models import Locationmap


class RegistrationDeviceSerializer(serializers.ModelSerializer):
    deviceid = serializers.IntegerField()
    device_model = serializers.CharField(max_length=255)
    app = serializers.CharField(max_length=50)
    version = serializers.CharField(max_length=255)

    class Meta:
        model = Device
        fields = ('deviceid', 'device_model', 'app', 'version')

    def create(self, validated_data):
        company = Company.objects.filter(user=validated_data.get('owner',
                                                                 None)).first()
        device_id_temp = validated_data.get('deviceid', None)
        if Device.objects.filter(deviceid=device_id_temp).first():
            raise serializers.ValidationError('This device id already exists!')
        else:
            device = Device.objects.create(company=company,
                                           deviceid=validated_data.get(
                                               'deviceid', None),
                                           device_model=validated_data.get(
                                               'device_model', None),
                                           app=validated_data.get('app', None),
                                           version=validated_data.get(
                                               'version', None))
        return device


class SaveDeviceDataSerializer(serializers.ModelSerializer):
    latitude = serializers.DecimalField(max_digits=9,
                                        decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9,
                                         decimal_places=6)
    device_id = serializers.IntegerField()
    data = serializers.JSONField()

    class Meta:
        model = Device
        fields = ('latitude', 'longitude', 'device_id', 'data')

    def create(self, validated_data):
        company = Company.objects.filter(user=validated_data.get(
            'owner', None)).first()
        device_id_temp = validated_data.get('device_id', None)
        device = Device.objects.filter(deviceid=device_id_temp).first()
        if device:
            if device.company == company:
                location = Location.objects.create(
                                           latitude=validated_data.get(
                                               'latitude', None),
                                           longitude=validated_data.get(
                                               'longitude', None),
                                           device=device,
                                           company=company,
                                           data=validated_data.get('data',
                                                                   None))
                locationmap = Locationmap.objects.filter(device=device).first()
                if locationmap:
                    Locationmap.objects.filter(device=device).update(
                                        latitude=validated_data.get(
                                            'latitude', None),
                                        longitude=validated_data.get(
                                            'longitude', None),
                                        data=validated_data.get('data', None))
                    locationmap = Locationmap.objects.filter(
                        device=device).first()
                    locationmap.save()
                else:
                    Locationmap.objects.create(
                                        latitude=validated_data.get(
                                            'latitude', None),
                                        longitude=validated_data.get(
                                            'longitude', None),
                                        device=device,
                                        company=company,
                                        data=validated_data.get('data', None))
            else:
                raise serializers.ValidationError(
                    'This device id does not belongs to the auth Company!')
        else:
            raise serializers.ValidationError(
                'This device id does not exists!')
        return location
