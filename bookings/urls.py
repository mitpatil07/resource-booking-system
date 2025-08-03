from django.urls import path
from .views import ResourceListCreateView, BookingCreateView, MyBookingsView

urlpatterns = [
    path('resources/', ResourceListCreateView.as_view(), name='resource_list'),
    path('book/', BookingCreateView.as_view(), name='book_resource'),
    path('mybookings/', MyBookingsView.as_view(), name='my_bookings'),
]
