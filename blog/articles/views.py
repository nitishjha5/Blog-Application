from django.shortcuts import render ,redirect 
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def articlelist(request):
	articles=Article.objects.all().order_by('date')
	return render(request,'articles/article_list.html',{ 'art': articles})

def articledetails(request,p):
	article=Article.objects.get(slug=p)
	return render(request,'articles/article_details.html',{ 'art': article})

@login_required(login_url= "/accounts/login/")
def articlecreate(request):
	if request.method=='POST':
		form=forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			#save to db
			return redirect('articles:list')

	else:
		form=forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form':form})

# Create your views here.
