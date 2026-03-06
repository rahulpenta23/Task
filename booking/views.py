from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot


# View function to display all available slots
def view_slots(request):

    slots = Slot.objects.all()

    service = request.GET.get("service")
    time = request.GET.get("time")

    if service:
        slots = slots.filter(name=service)

    if time:
        slots = slots.filter(time__icontains=time)

    return render(request, "slots.html", {"slots": slots})


# View function to book a slot
def book_slot(request, slot_id):

    slot = get_object_or_404(Slot, id=slot_id)

    slot.is_booked = True
    slot.save()

    return redirect("view_slots")


# View function to display booked slots
def booked_slots(request):

    slots = Slot.objects.filter(is_booked=True)

    return render(request, "booked_slots.html", {"slots": slots})