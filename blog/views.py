from django.shortcuts import render, redirect
from blog.forms import MessageForm
from blog.models import Messages


# Create your views here.o
def index(request):
    return render(request, 'index.html')
def single_post(request):
    return render(request, 'single-post.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

def category(request):
    return render(request, 'category.html')

