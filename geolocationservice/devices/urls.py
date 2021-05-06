from django.conf.urls import url
from .views import SaveDeviceDataView, GetLastDeviceDataView,\
    RegisterDeviceView


urlpatterns = [
    url('get_device_data', GetLastDeviceDataView.as_view()),
    url('register_device', RegisterDeviceView.as_view()),
    url('save_device_data', SaveDeviceDataView.as_view()),
    ]
