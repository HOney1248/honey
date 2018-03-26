from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import redirect, get_object_or_404


def post_list(request):
	posts=Post.objects.all()
	return render(request, 'lists.html', {'posts':posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.created = timezone.now()
			post.save()
			return redirect('anyword')
	else :
		form=PostForm()
		return render(request, 'new_post.html', {"form":form})

def post_detail(request,pk):
	post=get_object_or_404(Post, pk=pk)
	return render(request,'post details.html',{'post':post})

def edit_post(request,pk):
	templates= 'new_post.html'
	post=get_object_or_404(Post,pk=pk)
	if request.method=='POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form =PostForm(instance=post)
	context={
		'form':form,
		'post':post,

	}
	return render(request,templates,context)
def delete_post(request,pk):
	post=get_object_or_404(Post,pk=pk)
	post.delete()
	return HttpResponse("Deleted")