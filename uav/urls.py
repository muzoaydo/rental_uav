from django.conf.urls import urls
from uav import views

urlpatterns=[
    path('uav/', UAVList.as_view(), name='uav-list'),
    path('uav/<int:pk>/', UAVDetail.as_view(), name='uav-detail'),
]