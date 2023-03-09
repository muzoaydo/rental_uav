from django.shortcuts import get_object_or_404, redirect, render
from .models import UAV
from .serializers import UAVForm, UAVSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAdminUser
from rest_framework import generics


# UAV ListingAPI REST framework page view
class UAVAPIList(generics.ListCreateAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [IsAdminUser]

# UAV Details API REST framework page view
class UAVAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer
    permission_classes = [IsAdminUser]

# Listing and filtering of UAVS
def uavList(request):  
    uavs = UAV.objects.all().order_by('rented', 'id')

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

# UAV Create Page View
@login_required
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

# UAV Update Page View
@login_required
def uavUpdate(request, id):  
    uav = UAV.objects.get(id=id)
    form = UAVForm(initial={'brand': uav.brand, 'model': uav.model, 'weight': uav.weight, 'category': uav.category, 'rented': uav.rented,})
    if request.method == "POST":  
        form = UAVForm(request.POST, instance=uav)  
        if form.is_valid():  
            try:  
                form.save()
                model = form.instance
                return redirect('/rentUAV')  
            except Exception as e: 
                pass    
    return render(request,'uav_update.html',{'form':form})

# UAV Rent Page View
@login_required
def uavRent(request, id):
    uav = get_object_or_404(UAV, id=id)  # Get the UAV object with the given ID
    if request.method == "POST":
        uav.rented = True  # Set the rented field of the UAV object to True
        uav.save()  # Save the changes to the database
    return redirect('/rentUAV')

# UAV Delete Page View
@login_required
def uavDelete(request, id):
    uav = UAV.objects.get(id=id)
    try:
        uav.delete()
    except:
        pass
    return redirect('uav_list')
