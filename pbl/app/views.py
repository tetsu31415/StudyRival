from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Record
from .forms import PostForm


def login_form(request):
    return render(request, 'app/login.html', {})
def stop_watch(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    form = PostForm() 
    records = Record.objects.all()
    return render(request, 'app/stop_watch.html' , {'records': records, 'form': form, })

