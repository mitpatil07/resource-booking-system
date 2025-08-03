from rest_framework import generics, permissions, serializers
from .models import Resource, Booking
from .serializers import ResourceSerializer, BookingSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime
from django.http import HttpResponseBadRequest

from .models import Resource, Booking

from django.contrib import messages

@login_required
def index(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'booking':
            resource_id = request.POST.get('resource')
            quantity = int(request.POST.get('quantity'))
            start_time = parse_datetime(request.POST.get('start_time'))
            end_time = parse_datetime(request.POST.get('end_time'))

            try:
                resource = Resource.objects.get(id=resource_id)
            except Resource.DoesNotExist:
                return HttpResponseBadRequest("Resource not found.")

            if resource.available_quantity < quantity:
                return HttpResponseBadRequest("Not enough quantity.")

            resource.available_quantity -= quantity
            resource.save()

            Booking.objects.create(
                user=request.user,
                resource=resource,
                quantity=quantity,
                start_time=start_time,
                end_time=end_time
            )
            messages.success(request, "Resource booked successfully!")
            return redirect('home')

        elif form_type == 'add_resource':
            name = request.POST.get('name')
            description = request.POST.get('description')
            quantity = int(request.POST.get('available_quantity'))

            Resource.objects.create(name=name, description=description, available_quantity=quantity)
            messages.success(request, "Resource added successfully!")
            return redirect('home')

    resources = Resource.objects.all()
    bookings = Booking.objects.filter(user=request.user).select_related('resource')

    return render(request, 'bookings/index.html', {
        'resources': resources,
        'bookings': bookings
    })


class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated()] if self.request.method == 'POST' else []

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resource = serializer.validated_data['resource']
        quantity = serializer.validated_data['quantity']

        if quantity > resource.available_quantity:
            raise serializers.ValidationError("Not enough resources available.")

        resource.available_quantity -= quantity
        resource.save()
        serializer.save(user=self.request.user)

class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
