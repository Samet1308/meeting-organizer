from django import forms
from .models import Meeting

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['subject', 'date', 'start_time', 'end_time', 'participants']
