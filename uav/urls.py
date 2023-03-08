from django.urls import path
from uav import views
from django.views.generic.base import TemplateView

# URL paths for UAV pages
urlpatterns=[
    path('uavApi/', views.UAVList.as_view(), name='uav_list'),
    path('uavApi/<int:id>/', views.UAVDetail.as_view(), name='uav_detail'),
    path('uav/', TemplateView.as_view(template_name='uav_list.html'), name='uav_list'),
    path('uav_create/', TemplateView.as_view(template_name='uav_create.html'), name='uav_create'),
    path('uav_update/', TemplateView.as_view(template_name='uav_update.html'), name='uav_update'),
]