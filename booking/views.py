from django.shortcuts import render, redirect
from .models import Slot


def view_slots(request):

    slots = Slot.objects.all()

    service = request.GET.get("service")

    if service:
        slots = slots.filter(name=service)

    return render(request, "slots.html", {"slots": slots})


def book_slot(request, slot_id):

    slot = Slot.objects.get(id=slot_id)

    slot.is_booked = True
    slot.save()

    return redirect("view_slots")


def booked_slots(request):

    slots = Slot.objects.filter(is_booked=True)

    return render(request, "booked_slots.html", {"slots": slots})