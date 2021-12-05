from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from .models import Events, Profile, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

#from CondoMan import building


 # Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "building/home.html" )
    else:
        return HttpResponseRedirect(reverse("login"))



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "building/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "building/login.html")


def logout_view(request):
    logout(request)
    return render(request, "building/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "building/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "building/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "building/register.html")

@csrf_exempt
@login_required
def event(request):
    if request.method == 'POST':
        event = json.loads(request.body)

        type_of_event = event['event_type']
        place = event['place']
        date = event['date']

        print("aqui estoy")
        print(date)

        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)

        event = Events.objects.create(
            profile = profile,
            event_date = date,
            place = place,
            type_of_event = type_of_event,
            status = "Pending"
        )

        try:
            event.save()
        except:
            print("Error while saving in events")
            return JsonResponse({"message": "Error while saving in events"}, safe=False)

        return JsonResponse({"message": "200"}, safe=False)