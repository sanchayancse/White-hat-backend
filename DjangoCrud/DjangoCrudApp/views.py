from bson import ObjectId
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from DjangoCrudApp.models import Cricket
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_player(request):
    user_details = {"first_name": request.POST.get("first_name"), "last_name": request.POST.get("last_name")}
    post = Cricket(Cricketer_Name=request.POST.get("Cricketer_Name"), Cricketer_Age=request.POST.get("Cricketer_Age"),
                   Cricketer_Team_Name=request.POST.get("Cricketer_Team_Name"), Batsman=request.POST.get("Batsman"),
                   Bowler=request.POST.get("Bowler"),
                   No_of_catches=request.POST.get("No_of_catches"),
                   No_of_Matches=request.POST.get("No_of_Matches"),
                   Strike_Rate=request.POST.get("Strike_Rate"),
                   image=request.POST.get("image"),
                   user_details=user_details
                   )
    post.save()
    return HttpResponse("Data Inserted Successfully")



@csrf_exempt
def update_player(request, id):
    post = Cricket.objects.get(_id=ObjectId(id))
    post.user_details['first_name']= request.POST.get('first_name')
    post.save()
    return  HttpResponse("Data Updated")



def delete_player(request, id):
    post = Cricket.objects.get(_id = ObjectId(id))
    post.delete()
    return  HttpResponse("Data deleted Successfully")




def read_player(request, id):
    post = Cricket.objects.get(_id=ObjectId(id))
    stringval = "First Name: " + post.user_details['first_name'] + " Last name: " + post.user_details['last_name'],

    return HttpResponse(stringval)




def read_player_all(request):
    posts = Cricket.objects.all()
    stringval =""
    for post in posts:
        stringval += "First Name: " + post.user_details['first_name'] + " Last name: " + post.user_details['last_name'] + "<br>"
    return  HttpResponse(stringval)


