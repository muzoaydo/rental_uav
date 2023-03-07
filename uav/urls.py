from django.urls import path
from uav import views

# URL paths for UAV pages
urlpatterns=[
    path('uavApi/', views.UAVList.as_view(), name='uav-list'),
    path('uav/<int:pk>/', views.UAVDetail.as_view(), name='uav-detail'),
]