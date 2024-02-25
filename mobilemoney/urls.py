from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name = 'home'),
    path('createapiuser', views.createapiuser, name = 'createapiuser'),
    path('createapikey', views.createApiKey, name='createapikey'),
    path('getapiuserinfo', views.getCreatedUser, name = 'getapiuserinfos'),
    path('generateaccesstoken', views.generateAccessToken, name = 'generateaccesstoken'),
    path('requestpay', views.requestPay, name = 'requestpay'),
    path('requestpaystatus', views.requestToPayStatus, name = 'requestpaystatus'),

]