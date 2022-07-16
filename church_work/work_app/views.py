from django.shortcuts import get_object_or_404, redirect, render
from .models import myPost, myUser
from .forms import PostForm, UserForm
import datetime as dt

def home(request):
    ingposts = myPost.objects.filter().order_by('enddate')
    edposts = myPost.objects.filter().order_by('-enddate')
    posts = myPost.objects.filter().order_by('-writtendate')
    today = dt.datetime.now().date
    return render(request, 'home.html', {'ingposts':ingposts, 'edposts':edposts, 'posts':posts, 'today':today})

def create(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(myPost, pk = post_id)
    return render(request, 'detail.html', {'post_detail':post_detail})

def update_post(request, post_id):
    post = myPost.objects.get(id=post_id)

    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.enddate = form.cleaned_data['enddate']
            post.save()
            return redirect('detail', post_id)
    else:
        form = PostForm(instance = post)
        return render(request,'create.html', {'form':form})

def list_create(request):
    if (request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = UserForm()
    return render(request, 'list_create.html', {'form':form})

def update_list(request, list_id):
    user = myUser.objects.get(id=list_id)

    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user.name = form.cleaned_data['name']
            user.birthday = form.cleaned_data['birthday']
            user.phone = form.cleaned_data['phone']
            user.age = form.cleaned_data['age']
            user.save()
            return redirect('list')
    else:
        form = UserForm(instance = user)
        return render(request,'list_create.html', {'form':form})

def list(request):
    lists = myUser.objects.filter().order_by('name')
    return render(request, 'list.html', {'lists':lists})

def delete_post(request, post_id):
    post = get_object_or_404(myPost, pk = post_id)
    post.delete()
    return redirect('home')

def delete_list(request, list_id):
    list = get_object_or_404(myUser, pk = list_id)
    list.delete()
    return redirect('list')

def age_up(request):
    users = myUser.objects.all()
    for user in users:
        user.age += 1
        user.save()
    return redirect('list')

def age_down(request):
    users = myUser.objects.all()
    for user in users:
        user.age -= 1
        user.save()
    return redirect('list')

# Create your views here.
