from django.shortcuts import render
from blogs.models import Blogs

# index function
def home(request):
    blogs = Blogs.objects.all()
    return render(request, 'index.html',{'title':'Home','blogs':blogs})

