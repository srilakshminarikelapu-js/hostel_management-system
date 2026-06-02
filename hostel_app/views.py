from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .models import *
from .forms import *

from django.contrib.auth.models import User
from .models import RoomRegistration, Complaint, RoomAllocation

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import logout

from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


# Student Login
def student_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and not user.is_staff:

            login(request, user)

            return redirect('student_dashboard')

        return render(
            request,
            'student_login.html',
            {'error': 'Invalid Username or Password'}
        )

    return render(request, 'student_login.html')

# Admin Login
def admin_login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')

    return render(request, 'admin_login.html')


def student_dashboard(request):
    return render(request, 'student_dashboard.html')


def admin_dashboard(request):

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


def register_room(request):

    form = RoomRegistrationForm()

    if request.method == 'POST':
        form = RoomRegistrationForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.student = request.user
            room.save()

            return redirect('student_dashboard')

    return render(request,
                  'room_registration.html',
                  {'form': form})


def add_complaint(request):

    form = ComplaintForm()

    if request.method == 'POST':

        form = ComplaintForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.student = request.user
            obj.save()

            return redirect('student_dashboard')

    return render(request,
                  'add_complaint.html',
                  {'form': form})


def complaint_status(request):

    complaints = Complaint.objects.filter(
        student=request.user
    )

    return render(request,
                  'complaint_status.html',
                  {'complaints': complaints})


def view_registrations(request):

    registrations = RoomRegistration.objects.all()

    return render(
        request,
        'view_registrations.html',
        {'registrations': registrations}
    )


def view_complaints(request):

    complaints = Complaint.objects.all()

    return render(
        request,
        'view_complaints.html',
        {'complaints': complaints}
    )


def room_allocation(request):

    students = User.objects.filter(is_staff=False)

    if request.method == 'POST':

        student_id = request.POST['student']
        room_number = request.POST['room_number']

        student = User.objects.get(id=student_id)

        RoomAllocation.objects.create(
            student=student,
            room_number=room_number
        )

        return redirect('view_allocations')

    return render(request,
                  'room_allocation.html',
                  {'students': students})


def view_allocations(request):
    allocations = RoomAllocation.objects.all()
    return render(
        request,
        'view_allocations.html',
        {'allocations': allocations}
    )

def logout_view(request):

    logout(request)

    return redirect('home')

def update_complaint_status(request, id):

    complaint = Complaint.objects.get(id=id)

    if request.method == 'POST':

        complaint.status = request.POST['status']

        complaint.save()

    return redirect('view_complaints')

def my_room(request):

    allocation = RoomAllocation.objects.filter(
        student=request.user
    ).first()

    return render(
        request,
        'my_room.html',
        {'allocation': allocation}
    )

def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match.'
            )

            return redirect('register')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return redirect('register')

        if User.objects.filter(email=email).exists():

            messages.error(
                request,
                'Email already exists.'
            )

            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Registration successful. Please login.'
        )

        return redirect('student_login')

    return render(
        request,
        'register.html'
    )