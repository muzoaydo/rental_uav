from django.shortcuts import redirect, render
from rest_framework import generics
from .models import UAV
from .serializers import UAVForm, UAVSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters, mixins, viewsets
import django_filters.rest_framework
from .filters import ListingFilter

# UAV ListingAPI REST framework page view
class UAVAPIList(generics.ListCreateAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [IsAuthenticated]


# UAV Details API REST framework page view
class UAVAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [IsAuthenticated]

# Listing and filtering of UAVS
def uavList(request):  
    uavs = UAV.objects.all()

    # Get filter parameters
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    weight = request.GET.get('weight')
    category = request.GET.get('category')
    rented = request.GET.get('rented')

    # Filter uavs based on parameters
    try:
        if brand is not "":
            uavs = uavs.filter(brand__icontains=brand)
        if model is not "":
            uavs = uavs.filter(model__icontains=model)
        if weight is not "":
            weight = float(weight)
            uavs = uavs.filter(weight=weight)
        if category is not "":
            uavs = uavs.filter(category__icontains=category)
        if rented is not "":
            uavs = uavs.filter(rented=rented)
    except Exception as e:
        print(e)

    return render(request, 'uav_list.html', {'uavs': uavs})

def uavCreate(request):  
    if request.method == "POST":  
        form = UAVForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('uav_list')  
            except:  
                pass  
    else:  
        form = UAVForm()  
    return render(request,'uav_create.html',{'form':form})  


def uavUpdate(request, id):  
    uav = UAV.objects.get(id=id)
    form = UAVForm(initial={'brand': uav.brand, 'model': uav.model, 'weight': uav.weight, 'category': uav.category, 'rented': True,})
    if request.method == "POST":  
        form = UAVForm(request.POST, instance=uav)  
        if form.is_valid():  
            try:  
                form.save()
                model = form.instance
                return redirect('/hireUAV')  
            except Exception as e: 
                pass    
    return render(request,'uav_update.html',{'form':form})  


def uavDelete(request, id):
    uav = UAV.objects.get(id=id)
    try:
        uav.delete()
    except:
        pass
    return redirect('uav_list')
