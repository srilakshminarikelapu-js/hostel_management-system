from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import RoomRegistration, Complaint, RoomAllocation


def admin_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not request.user.is_staff:
        return redirect('student_dashboard')

    context = {

        'total_students':
        User.objects.filter(is_staff=False).count(),

        'total_registrations':
        RoomRegistration.objects.count(),

        'total_complaints':
        Complaint.objects.count(),

        'total_allocations':
        RoomAllocation.objects.count(),

    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )