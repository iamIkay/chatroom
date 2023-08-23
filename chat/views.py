from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    rooms = Room.objects.all()

    if(rooms.filter(name=room_name).exists()):
        print("Room exists!!")
    else:
        room = Room.objects.create(name=room_name)
        room.save()

    return redirect('/'+room_name+'/?username='+username)


def room(request, room_name):
    username = request.GET.get('username')
    room = Room.objects.get(name=room_name)

    return render(request, 'room.html', {'username':username, 'room': room})

def send(request):
    print("CALLING REQUEST!!!")
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']

    new_message = Message.objects.create(message=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse("Message sent successfully!")

def getMessages(request,room_id):
    messages = Message.objects.filter(room=room_id)

    return JsonResponse({"messages":list(messages.values())})