from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
from .forms import MeetingForm

# Create your views here.



def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting-list.html', {'meetings': meetings})

def meeting_create(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting-list')
    else:
        form = MeetingForm()
    return render(request, 'meeting-form.html', {'form': form})

def meeting_update(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting-list')
    else:
        form = MeetingForm(instance=meeting)
    return render(request, 'meeting-form.html', {'form': form})

def meeting_delete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == "POST":
        meeting.delete()
        return redirect('meeting-list')
    return render(request, 'meeting-confirm-delete.html', {'meeting': meeting})
