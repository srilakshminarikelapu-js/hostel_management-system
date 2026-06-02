from django.db import models
from django.contrib.auth.models import User


class RoomRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.username


class Complaint(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return self.student.username


class RoomAllocation(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    allocated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.room_number}"

class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=15)

    address = models.TextField()

    def __str__(self):
        return self.user.username