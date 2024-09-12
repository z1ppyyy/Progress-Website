from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    """Show main page"""
    content = Post.objects.all()
    return render(request, "index.html", {"content": content})

def progress(request):
    """Handle the progress posting"""
    if request.method == "POST":
        progress = request.POST['progress']
        hours = request.POST['hours']
        minutes = request.POST['minutes']

        if hours is None:
            post = Post(progress=progress, minutes=minutes)
            post.save()
            return redirect("index")
        elif minutes is None:
            post = Post(progress=progress, hours=hours)
            post.save()
            return redirect("index")
        else:
            post = Post(progress=progress, hours=hours, minutes=minutes)
            post.save()
            return redirect("index")
        
    return render(request, "post.html")