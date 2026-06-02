from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('student-login/', views.student_login, name='student_login'),
    path('admin-login/', views.admin_login_view, name='admin_login'),

    path('student-dashboard/', views.student_dashboard,
         name='student_dashboard'),

    path('admin-dashboard/', views.admin_dashboard,
         name='admin_dashboard'),

    path('register-room/', views.register_room,
         name='register_room'),

    path('add-complaint/', views.add_complaint,
         name='add_complaint'),

    path('complaint-status/',
         views.complaint_status,
         name='complaint_status'),

    path('view-registrations/',
         views.view_registrations,
         name='view_registrations'),

    path('view-complaints/',
         views.view_complaints,
         name='view_complaints'),

    path('room-allocation/',
         views.room_allocation,
         name='room_allocation'),

    path('view-allocations/',
         views.view_allocations,
         name='view_allocations'),

    path(
    'logout/',
    views.logout_view,
    name='logout'),

    path(
    'update-complaint/<int:id>/',
    views.update_complaint_status,
    name='update_complaint_status'),

    path(
    'my-room/',
    views.my_room,
    name='my_room'),

    path(
    'register/',
    views.register,
    name='register'),
]