from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Neighborhood,Profile,Post,Business
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm,NeighborhoodForm,BusinessForm,PostForm


# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    hoods = Neighborhood.objects.all()
    profile = Profile.objects.all()
    print(profile)
    return render(request, 'index.html',{'hoods':hoods})



@login_required(login_url='/accounts/login')
def profile(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    hoods = Neighborhood.objects.filter(id=id)
    posts = Post.objects.filter(user_id=id)
   
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)   
    else:
    
        return render(request, 'profile.html',{"user":user, "profile":profile, 'hoods':hoods, "posts":posts})


@login_required(login_url='/accounts/login/')
def update_profile(request,id): 
    current_user = request.user
    user = User.objects.get(id=id)
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id =request.user.id
            profile.save()
        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"user": user, "form": form})  

@login_required(login_url='/accounts/login')
def neighborhood(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    name = Neighborhood.objects.filter(id = id)
    try:
        neighborhood = Neighborhood.objects.get(neighborhood_id=id)
    except ObjectDoesNotExist:
        return redirect(index_html, current_user.id)   
    
    return render(request, 'index.html', {"user":user, "name":name, "neighborhood":neighborhood, "current_neighborhood":current_neighborhood})




@login_required(login_url='/accounts/login')
def join(request, id):
    current_user = request.user
    form = NeighborhoodForm() 
    
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            print(neighborhood)
            neighborhood.user_id =request.user.id
            neighborhood.save()

        return redirect(home)

    else:
        form = NeighborhoodForm()                    
        
    return render(request, 'neighborhood.html', {"user": current_user, "form": form})  


@login_required(login_url='/accounts/login')
def business(request, id):
    
    try:
        neighborhood = Neighborhood.objects.get(id=id)
    except ObjectDoesNotExist:
        return redirect(index_html, current_user.id)
    
    businesses = Business.objects.filter(business_neighborhood_id=id)
    posts = Post.objects.filter(location_id=id)
    hoods = Neighborhood.objects.filter(id=id)
    print(posts)
    return render(request, 'business.html',{'businesses':businesses,'posts':posts,'hoods':hoods })


@login_required(login_url='/accounts/login')
def add_business(request, id):

    current_user = request.user
    try:
        profile = Profile.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)   
    current_neighborhood = Neighborhood.objects.get(id = id)
    print(current_neighborhood)
    current_user = request.user
    form = BusinessForm()   
    
