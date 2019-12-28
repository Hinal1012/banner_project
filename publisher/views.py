from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .forms import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.decorators import login_required
import random

# Create your views here.
def home(request):
    return render(request, 'publisher/index.html')

def register(request):
    if request.method == 'POST':
        is_client = request.POST.get('is_client')
        if is_client is not None:
            is_client = True
        else:
            is_client = False
        is_publisher = request.POST.get('is_publisher')
        if is_publisher is not None:
            is_publisher = True
        else:
            is_publisher = False
        first_name = request.POST.get('first_name')
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        # phone_num = request.POST['phone_num']
        # address = request.POST['address']

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Sorry! This email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=email, first_name=first_name, email=email, password=pass1, is_client=is_client, is_publisher=is_publisher)
                user.save()
                return redirect(banners)
        else:
            messages.info(request, 'Password not matching')
            return redirect(register)
    else:
        return render(request, 'publisher/register.html')

def admin_panel(request):
    if request.method == 'GET':
        x = Banners_details.objects.filter(name=request.user) 
    return render(request, 'publisher/admin-panel/index.html', {'data': x})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['password']
        user = auth.authenticate(username=email, password=pass1)
        if user is not None:
            auth.login(request, user)
            # print(request.user.is_publisher)
            if User.objects.filter(email=email).exists() and request.user.is_publisher==True:
                return redirect(admin_panel)
                # return HttpResponse('Welcome to publisher admin panel')
            else:
                return redirect(banners)
            return redirect(banners)
        else:
            messages.info(request, 'Invalid credential')
            return redirect(login)
    else:
        return render(request, 'publisher/login.html')

def logout(request):
    auth.logout(request)
    return redirect(banners)

@login_required(login_url='/publisher/login/')
def banner_details(request):
    form = BannerDetailsForm
    if request.method == 'POST':
        form = BannerDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            count = Banners_details.objects.count()
            # print('count:', str(count))
            post = form.save(commit=False)
            post.id = random.randint(100000,999999)
            # print('post-id: ', post.id)
            post.name = request.user #{{ user.first_name}}
            post.save()
            return redirect(admin_panel)
    return render(request, 'publisher/admin-panel/add-bannerform.html', {'form': form})

def banners(request):
    if request.method == 'GET':
        banner_list = Banners_details.objects.all()
        user_list = User.objects.all()
    return render(request, 'publisher/index.html', {'data': banner_list, 'publiss': user_list})

def banners_current_user(request):
    if request.method == 'GET':
        x = Banners_details.objects.filter(name=request.user) 
    return render(request, 'publisher/admin-panel/banners_publisherwise.html', {'data': x})

def banners_publisherwise(request, id):
    if request.method == 'GET':
        x = Banners_details.objects.all
        y = User.objects.filter(id=id)
    # return render(request, 'publisher/banners_current_user.html', {'banners': x, 'publishers': y})
    return render(request, 'publisher/publisher_page/mycompanybanner.html', {'banners': x, 'publishers': y})

def delete_baanner(request, id):
    banner_del = Banners_details.objects.get(id = id)
    banner_del.delete()
    return redirect (banners_publisherwise)

def update_banner_details(request, id):
    details_update = Banners_details.objects.get(id = id)
    # print(details_update)
    if request.method == 'POST':
        obj = BannerDetailsForm(request.POST, instance=details_update)
        if obj.is_valid():
            obj.save()
            return redirect (banners_publisherwise)
    obj = BannerDetailsForm(instance=details_update)
    return render(request, 'publisher/admin-panel/update-banner.html', {'data':obj})

def update_user_details(request, id):
    user_update = User.objects.get(id=id)
    if request.method == 'POST':
        obj = UserDetailsForm(request.POST, request.FILES, instance=user_update)
        if obj.is_valid():
            obj.save()
            return redirect(admin_panel)
    obj = UserDetailsForm(instance=user_update)
    return render(request, 'publisher/update_userdetails.html', {'data':obj}) 