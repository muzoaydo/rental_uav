from django.urls import path
from uav import views
from django.views.generic.base import TemplateView

# URL paths for UAV pages
urlpatterns=[
    path('uavApi/', views.UAVAPIList.as_view(), name='uav_api'),
    path('uavApi/<int:pk>/', views.UAVAPIDetail.as_view(), name='uav_detail'),
    path('hireUAV/', views.uavList, name='uav_list'),
    path('uav_create/', views.uavCreate, name='uav_create'),
    path('uav_update/<int:id>/', views.uavUpdate, name='uav_update'),
    path('uav_delete/<int:id>/', views.uavDelete, name='uav_delete'),
]