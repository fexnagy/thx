from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    
    rooms = Room.objects.filter(name__icontains=q)

    # rooms = Room.objects.all()
    context = {"rooms": rooms, "title": "Home"}
    return render(request, "base/home.html", context)


def room(request, id):
    room = Room.objects.get(id=id)
    context = {"room": room, "title": room.name}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()

    # Save to the database
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form, "title": "Create"}
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
