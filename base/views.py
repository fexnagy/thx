from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room
from .forms import RoomForm


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(
        Q(name_client__icontains=q)
        | Q(comment__icontains=q)
    )

    room_count = rooms.count()
    context = {"rooms": rooms, "room_count": room_count, "title": "Home"}
    return render(request, "base/home.html", context)


def room(request, id):
    room = Room.objects.get(id=id)
    context = {"room": room, "title": room.name_client}
    return render(request, "base/room.html", context)


def submitRoom(request):
    form = RoomForm()

    # Save to the database
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form, "title": "Submit"}
    return render(request, "base/form.html", context)


def editRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    # Save to the database
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form, "room": room, "title": "Edit"}
    return render(request, "base/form.html", context)


def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    # Delete room from the database
    if request.method == "POST":
        room.delete()
        return redirect("home")

    context = {"room": room, "title": "Delete"}
    return render(request, "base/delete.html", context)
