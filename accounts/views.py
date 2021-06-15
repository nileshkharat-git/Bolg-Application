from django.contrib.auth import authenticate, login,logout
from django.contrib.messages import success,error,warning
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogs.models import Blogs
from blogs.forms import BlogForm
from .models import Accounts


# user creation function/view
def user_signup(request):
    if request.POST:
        if request.POST['password'] != request.POST['cnfpassword']:
            error(request,'Password not matching!')
            return redirect('/')
        else:
            user = Accounts.object.create_user(
                email=request.POST['email'],
                username=request.POST['username'],
                first_name=request.POST['firstName'],
                last_name=request.POST['lastName'],
                password=request.POST['password'],
            )
            user.save()
            return redirect('/')
    return render(request, 'user/signup.html', {'title': 'Signup'})


# user login view
def user_login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        return redirect('/')
    else:
        warning(request,'Login failed')
        return redirect('/')

# user dashboard view
@login_required(login_url='/')
def dash_board(request):
    form = BlogForm()
    myBlogs = Blogs.objects.all().filter(user = request.user )
    context = {'form': form, 'title': 'Dashboard', 'myBlogs':myBlogs}
    return render(request, 'user/dashBoard.html', context)


# user logout view
@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')
