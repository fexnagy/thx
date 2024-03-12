from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms, "title": "Home"}
    return render(request, "base/home.html", context)


def room(request, id):
    room = Room.objects.get(id=id)
    context = {"room": room, "title": room.name}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm()

    # Send the form to the database
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form, "title": "Create Room"}
    return render(request, "base/form.html", context)


def editRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    context = {"form": form, "title": "Edit Room"}
    return render(request, "base/form.html", context)
