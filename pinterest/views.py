from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UploadImage,CommentForm
from .models import ImageFile,Comment
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger



def handler404(request,exception):
    return render(request, '404.html', status=404)
def handler500(request):
    return render(request, '500.html', status=500)



# Create your views here.

def index(request):
	pins = ImageFile.objects.all().order_by('-created')
	context = {
	'pins':pins	
	}
	return render(request,'pinterest/index.html',context)

# -------------------------------------------------------------

@login_required(login_url='login')
def pinDetail(request,id):
	pin=ImageFile.objects.filter(sno=id).first()
	comments= Comment.objects.filter(pin=pin)

	template = 'pinterest/view_image.html'
	context = {
	'details':pin,
	'comments':comments,
	}
	return render(request,template,context)

# ---------------------------------------------------------------

# edit pin
@login_required(login_url='login')
def editPin(request,id):
	pin = ImageFile.objects.get(sno=id)
	form = UploadImage(instance=pin)
	if request.method == 'POST':
		form = UploadImage(request.POST,request.FILES,instance=pin)
		if form.is_valid():
			form.save()
			return redirect('profile')
	context = {
		'form':form,
		'pin':pin
		}
	return render(request,'pinterest/update-pin.html',context)


# ---------------------------------------------------------------

@login_required(login_url='login')
def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        pin= ImageFile.objects.get(sno=postSno)
        comment=Comment(comment= comment, user=user, pin=pin)
        comment.save()
        # messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/pin/{pin.sno}")

@login_required(login_url='login')
def uploadImage(request):
	form = UploadImage()
	if request.method == 'POST':
			form = UploadImage(request.POST,request.FILES)
			if form.is_valid():
					instance = form.save(commit=False)
					# print(instance)
					instance.author = request.user
					instance.save()
					return redirect('profile')
	context = {
	'form':form
	}
	return render(request,'pinterest/AddPin.html',context)

@login_required(login_url='login')
def profile(request):
	user = request.user
	mypins = ImageFile.objects.filter(author=user).order_by('-created')
	count = ImageFile.objects.filter(author=user).count()


	# paginator = Paginator(mypins, 3) # Show 25 contacts per page.

	# page_number = request.GET.get('page',3)
	# page_obj = paginator.get_page(page_number)



	context = {
	'pins':mypins,	
	'user':user,
	'count':count
	}
	template = 'pinterest/profile.html'
	return render(request,template,context)

@login_required(login_url='login')
def details(request,id):
	pin=ImageFile.objects.filter(sno=id).first()
	comments= Comment.objects.filter(pin=pin)

	template = 'pinterest/mypins.html'
	context = {
	'details':pin,
	'comments':comments,
	}
	return render(request,template,context)


