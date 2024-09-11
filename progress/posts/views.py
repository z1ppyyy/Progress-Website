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
        spent = request.POST['spent']

        post = Post(progress=progress, spent=spent)
        post.save()
        return redirect("index")
    return render(request, "post.html")