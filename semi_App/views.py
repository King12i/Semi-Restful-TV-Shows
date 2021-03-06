from django.shortcuts import render, redirect,HttpResponse
from .models import Tv_Show

# Create your views here.

def index(request):
    
    return render(request, "index.html")

def Add_new_show(request): 

    return render(request, "add_new_show.html")

def Create_Show(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    descriptions = request.POST['descriptions']
    create_show= Tv_Show.objects.create(title= title, network= network, release_date= release_date, descriptions= descriptions)
    

    return redirect(f"/show/{ create_show.id }")


def tv_show(request, Id):

    daitel_id = Tv_Show.objects.get(id=Id)
    context ={

        "show_info": daitel_id
    }


    return render(request, "tv_shows2.html", context)

def all_show(request):
    
    all_data= Tv_Show.objects.all()

    context= {

        "data_in_Db":all_data
    }
    
    return render(request, "all_shows.html", context)

# This is for Editing

def edit_a_show(request, ed):
        
    all_data= Tv_Show.objects.get(id=ed)

    context ={
        "contex":all_data
    }
   
    return render (request, "edit_show.html", context)

def update_a_show(request, ed):
    detail = Tv_Show.objects.get(id=ed)
    detail.title = request.POST['title']
    detail.network = request.POST['network']
    detail.release_date = request.POST['release_date']
    detail.descriptions = request.POST['descriptions']
    detail.save()
    return redirect(f"/show/{ed}")

def del_show(request, Id):
    daitel_id = Tv_Show.objects.get(id=Id)
    context ={

        "show_info": daitel_id
    }
    return render(request,"delete_show.html", context)

def show_delete(request, Id):
    some_element = Tv_Show.objects.get(id=Id)
    some_element.delete()

    return redirect("/all_show")
