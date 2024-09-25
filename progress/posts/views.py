from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from users.models import Profile


@login_required(login_url='/login')
def index(request):
    """Show main page"""
    content = list(Post.objects.all())[::-1]
    return render(request, "index.html", {"content": content, "requested": request.user})


def progress(request):
    """Handle the progress posting"""
    if request.method == "POST":
        user_object = Profile.objects.get(user=request.user)
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
                minutes=minutes,
            )
            post.save()
            posts = Post.objects.all()[::-1]
            for index, post in enumerate(posts):
                try:
                    if (posts[index].date - posts[index].date):
                        continue
                    elif (posts[index].date - posts[index].date) != 1:
                        # Kill streak
                        user_object = Profile.objects.get(user=request.user)
                        user_object.streak = 0
                        break
                    else:
                        user_object = Profile.objects.get(user=request.user)
                        user_object.streak += 1
                except:
                    pass
            user_object.streak += 1
            user_object.save()
            return redirect("index")

    return render(request, "post.html")


def post_id(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'post_id.html', {'posts': posts, "requested": request.user})

def delete_post(request, id):   
    post_to_delete = Post.objects.get(id=id)
    if request.user == post_to_delete.user:
        post_to_delete.delete()
    else:
        return HttpResponse("You are not the owner of this post. <a href='/'>Back to Home Page</a>")
    return redirect("index")

def edit_post(request, id):
    post_obj = Post.objects.get(id=id)
    if request.method == "POST":
        progress = request.POST['progress']
        hours = request.POST['hours']
        minutes = request.POST['minutes']

        if len(hours) < 1:
            error = "Please enter hours"
            return render(request, "post.html", {"error": error, "post": post_obj})
        elif len(progress) < 10:
            error = "The length of progress should be at least 10 characters."
            return render(request, "post.html", {"error": error, "post": post_obj})
        elif int(hours) > 23 or int(hours) < 1 or int(minutes) < 0 or int(minutes) > 59:
            error = "Please enter valid time spent"
            return render(request, "post.html", {"error": error, "post": post_obj})
        else:
            post_obj.progress = progress
            post_obj.hours = hours
            post_obj.minutes = minutes
            post_obj.save()
            return redirect("index")
    else:
        if request.user == post_obj.user:
            return render(request, "post.html", {"post": post_obj})
        else:
            return HttpResponse("You are not the owner of this post. <a href='/'>Back to Home Page</a>")