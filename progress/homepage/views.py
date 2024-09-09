from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def progress(request):
    
    current_date = date.today().strftime('%B %d')
    if request.method == "POST":
        progress = request.POST['progress']
        spent = request.POST['spent']
        content = {
            "progress": progress,
            "spent": spent,
            "time": current_date
        }
        return render(request, "index.html", content)
    return render(request, "post.html")