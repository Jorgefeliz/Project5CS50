import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from .models import Announcement, Events, Issues, Profile, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from datetime import date
from django.db.models import Q

#from CondoMan import building


 # Create your views here.

def index(request):
    if request.user.is_authenticated:

        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)
        today = date.today()


        if profile.role == "admin":
            eventos = Events.objects.filter(status = "Pending").order_by("event_date")

            #This is because I desided that admin must see announces 30 days before today, 
            # it's like a history of the most recent past announces

            days = datetime.timedelta(30)
            today = today - days
            announces = Announcement.objects.filter(valid_date__gte = today  )

            issues = Issues.objects.filter(~Q(status = "solved"))

            return render(request, "building/homeadmin.html", {"events": eventos, "announces": announces, "issues": issues })

         ############################################################################333   

        eventos = Events.objects.filter(profile = profile).filter(event_date__gte = today).order_by("event_date")
        
        announces = Announcement.objects.filter(valid_date__gte = today  )

        issues = Issues.objects.filter(reported_by = profile)

        return render(request, "building/home.html", {"events": eventos, "announces": announces, "issues":issues })
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


        residencial = request.POST["residencial"]
        building = request.POST["building"]
        apto = request.POST["apto"]


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
            profile = Profile.objects.create(
                user = user,
                residencial = residencial,
                building = building,
                apto = apto    )
            
            profile.save()

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
        date = event['date'] + "T08:00"

 

        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)

        #making sure there is not events same day and same location
        
      
        
        comprobar = Events.objects.filter(place=place).filter(event_date=date)

        if len(comprobar) != 0:
            return JsonResponse({"message": "There is an event in that date and place"}, safe=False)

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

        return JsonResponse({"message": "The event have been created"}, safe=False)


@login_required
def event_update(request, event_id, status):
    if request.method == 'GET':
     
        try:
            evento = Events.objects.get(pk=event_id)
            evento.status = status
            evento.save()
            
        except:
            print("Error while updating in events")
            return JsonResponse({"message": "Error while updating in events"}, safe=False)

        return JsonResponse({"message": "The event have been updated"}, safe=False)

@csrf_exempt
@login_required
#the announcement is create it
def announcement (request):
    if request.method == "POST":
        announce = json.loads(request.body)

        title = announce['title']
        content = announce['content']
        valid_date = announce['valid_date']


        try:
            user = User.objects.get(pk=request.user.id)
            profile = Profile.objects.get(user=user)

            announcement = Announcement.objects.create(
                profile = profile,
                title = title,
                content = content,
                valid_date = valid_date
                 )
            announcement.save()
            
        except:
            print("Error while creating announcement")
            return JsonResponse({"message": "Error while creating announcement"}, safe=False)

        return JsonResponse({"message": "The announcement have been updated", "announce_id": announcement.id }, safe=False)


@csrf_exempt
@login_required
#update (POST) or delete (PUT) announcement
def announcement_update (request):
        if request.method == 'POST':
            announce = json.loads(request.body)
            announce_id = announce['announce_id']
            title = announce['title']
            content = announce['content']
            valid_date = announce['valid_date']
        

            try:
             
                datetime.datetime.strptime(valid_date,'%Y-%m-%d')
        
            except:
                valid_date = 0
        

            try:
                announcement = Announcement.objects.get(pk=announce_id)

                announcement.title = title
                announcement.content = content

                if valid_date == 0:
                   announcement.save()
                else:
                    announcement.valid_date = valid_date
                    announcement.save()
                
            except:
                print("Error while updating announce")
                return JsonResponse({"message": "Error while updating announce"}, safe=False)

            return JsonResponse({"message": "The annouce have been updated"}, safe=False)

        if request.method == 'PUT':
     
            announce = json.loads(request.body)

            pk = announce['announce_id']
       
            try:
                announcement = Announcement.objects.get(pk=pk)
                announcement.delete()
                
                
            except:
                print("Error while deleting announces")
                return JsonResponse({"announcement": "Error while deleting announces"}, safe=False)

            return JsonResponse({"message": "Announcement deleted"}, safe=False)

@csrf_exempt
@login_required
def announcement_retrieve (request):
        if request.method == 'POST':
            announce = json.loads(request.body)

            announce_id = announce['announce_id']
     
            try:
                announcement = Announcement.objects.get(pk=announce_id)

                 
            except:
                print("Error while retrieving announce")
                return JsonResponse({"message": "Error while retrieving announce"}, safe=False)

            return JsonResponse(announcement.serialize(), safe=False)

@csrf_exempt
@login_required
##POST create
##PUT update
##GET retrieve
def issue(request, issue_id):
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)

        issue = json.loads(request.body)
        
        
        title = issue["title"]
        categoria = issue["categoria"]
        description = issue["description"]
        status = issue["status"]
        reported_by = profile
        print(issue)


        try:
            issues = Issues.objects.create(
                title = title,
                categoria = categoria,
                description = description,
                reported_by = reported_by,
                status = status
            )
            issues.save()

        except:
            return JsonResponse({"message": "Error while creating report"}, safe=False)
        
        return JsonResponse({"message": "Report created"}, safe=False)


    if request.method == "PUT":

        user = User.objects.get(pk=request.user.id)
        profile = Profile.objects.get(user=user)

        issue = json.loads(request.body)

        issue_id = issue["id"]
        status = issue["status"]
        signed_by = profile
        signed_date = date.today()
        print("estamos AKI")

        try:
            description = issue["description"]
        except:
            description = None

        try:
            issues = Issues.objects.get(pk=issue_id)

            if description == None:
                pass
            else:
                issues.description = description

            issues.signed_by = signed_by
            issues.status = status
            signed_date = signed_date
            
            issues.save()            

        except:
            return JsonResponse({"message": "Error while updating report"}, safe=False)


        return JsonResponse({"message": "Report updated"}, safe=False)

    if request.method == "GET":

        try:
            issues = Issues.objects.get(pk = issue_id)
        except:
            return JsonResponse({"message": "Error while retrieving report"}, safe=False)
        
        return JsonResponse(issues.serialize(), safe=False)
        
