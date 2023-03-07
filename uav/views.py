from rest_framework import generics
from .models import UAV
from .serializers import UAVSerializer

# UAV Listing page view
class UAVList(generics.ListCreateAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

# UAV Details page view
class UAVDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer