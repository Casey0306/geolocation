from django.conf.urls import url
from .views import CreateTokenView, GetTokenView


urlpatterns = [
    url('new_token', CreateTokenView.as_view()),
    url('get_token', GetTokenView.as_view()),
    ]
