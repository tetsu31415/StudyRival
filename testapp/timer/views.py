from django.shortcuts import render
from .models import Record
from .forms import PostForm

# Create your views here.

def test_view(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    form = PostForm()	
    records = Record.objects.all()
    return render(request, 'timer/stop_watch.html', {'records': records, 'form': form, })


