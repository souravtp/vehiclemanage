from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import VehicleSerializer
from .models import Vehicle
from .permissions import IsSuperAdmin, IsAdmin


# Create your views here.


class VehicleCreateView(generics.CreateAPIView):
    permission_classes = [IsSuperAdmin]
    serializer_class = VehicleSerializer


class VehicleListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleUpdateView(generics.UpdateAPIView):
    permission_classes = [IsSuperAdmin | IsAdmin]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class VehicleDeleteView(generics.DestroyAPIView):
    permission_classes = [IsSuperAdmin]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
