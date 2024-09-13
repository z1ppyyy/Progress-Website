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

        if len(hours) < 1:
            return redirect("index")
        elif len(progress) < 10:
            return redirect("index")
        elif int(hours) > 23 or int(hours) < 1 or int(minutes) < 0 or int(minutes) > 59:
            return redirect("index")
        else:
            post = Post(progress=progress, hours=hours, minutes=minutes)
            post.save()
            return redirect("index")
        
    return render(request, "post.html")