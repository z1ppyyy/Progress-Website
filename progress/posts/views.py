from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from users.models import Profile


@login_required(login_url='/login')
def index(request):
    """Show main page"""
    content = list(Post.objects.all())[::-1]
    return render(request, "index.html", {"content": content})


def progress(request):
    """Handle the progress posting"""
    if request.method == "POST":
        # user_object = Profile.objects.get(id=request.user.id)
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
            posts = Post.objects.all()[::-1]
            for index, post in enumerate(posts):
                try:
                    if (posts[index].date - posts[index].date):
                        continue
                    elif (posts[index].date - posts[index].date) != 1:
                        # Kill streak
                        user_object = Profile.objects.get(id=request.user.id)
                        user_object.streak = 0
                        break
                    else:
                        user_object = Profile.objects.get(id=request.user.id)
                        user_object.streak += 1
                except:
                    pass
            # user_object.streak += 1
            # user_object.save()

            # Logic to check if its a streak
            # print(Profile.objects.get(id=request.user.id).streak)
            return redirect("index")

    return render(request, "post.html")


def post_id(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post_id.html', {'posts': posts})
