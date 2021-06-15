from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.messages import info,error
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts
from .models import Blogs
from .forms import BlogForm
import datetime

# blog creation view
@login_required(login_url='/')
def published_blog(request):
    if request.method == 'POST':
        user = Accounts.object.get(email=request.user.email)
        if user:
            Blogs.objects.create(user= user, title= request.POST['title'],article= request.POST['article'])
            info(request,f'Blog has been published on {datetime.datetime.now().date()}')
            return redirect('/users/dashboard')
        else:
            error(request,'Sorry! user not matching')
            return redirect('/users/dashboard')
    else:
        return redirect('/users/dashboard')

# blog read function
def read_blog(request,blogID):
    blog = get_object_or_404(Blogs,id=blogID)
    return render(request,'blogs/readBlog.html',{'blog':blog,'title':'read blog'})

# search blogs by query
def show_by_query(request):
    query = request.GET['query']
    titles = Blogs.objects.values_list('title')
    foundedBlogs = list()
    for title in titles:
        head = title[0]
        if head.lower().find(query.lower()) != -1:
            blog = Blogs.objects.filter(title=head)
            foundedBlogs.append(blog)
        else:
            continue
    return render(request,'blogs/searchPage.html',{'foundBlogs':foundedBlogs,'title':'search page'})


# user like function/view
@login_required(login_url='/')
def hit_like(request,bid):
    blog = get_object_or_404(Blogs,id=bid)
    blog.likes.add(request.user)
    blog.save()
    return redirect(read_blog,blogID=bid)

# Edit blog view
def edit_blog(request):
    if request.POST:
        blog = get_object_or_404(Blogs,id=request.POST['id'])
        blog.title = request.POST['title']
        blog.article = request.POST['article']
        blog.save()
        info(request,"Blog has been updated.")
        return redirect('/users/dashboard')
    instance = get_object_or_404(Blogs,id=request.GET['id'])
    return render(request,'blogs/editBlog.html',{'instance':instance})

# Delete Blog
def delete_blog(request):
    blog = get_object_or_404(Blogs,id = request.GET['id'])
    blog.delete()
    info(request,"Blog removed successfully.")
    return redirect('/users/dashboard')