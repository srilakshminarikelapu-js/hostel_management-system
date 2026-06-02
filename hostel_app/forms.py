from django import forms
from .models import RoomRegistration, Complaint

class RoomRegistrationForm(forms.ModelForm):
    class Meta:
        model = RoomRegistration
        fields = ['room_type']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text']