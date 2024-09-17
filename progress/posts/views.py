from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
@login_required(login_url='/login')
def index(request):
    """Show main page"""
    content = list(Post.objects.all())[::-1]
    return render(request, "index.html", {"content": content})

def progress(request):
    """Handle the progress posting"""
    if request.method == "POST":
        progress = request.POST['progress']
        hours = request.POST['hours']
        minutes = request.POST['minutes']

        if len(hours) < 1:
            error = "Please enter hours"
            return render(request, "post.html", {"error": error})
        elif len(progress) < 10:
            error = "The length of progress should be at least 10 characters."
            return render(request, "post.html", {"error": error})
        elif int(hours) > 23 or int(hours) < 1 or int(minutes) < 0 or int(minutes) > 59:
            error = "Please enter valid time spent"
            return render(request, "post.html", {"error": error})
        else:
            post = Post(
                user=request.user, 
                progress=progress, 
                hours=hours, 
                minutes=minutes
            )
            post.save()
            return redirect("index")
        
    return render(request, "post.html")

def post_id(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post_id.html', {'posts': posts})