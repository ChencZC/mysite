from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.template.loader import get_template

# Create your views here.

def homepage(request):
	template = get_template('index.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	#post_lists = list()
	#for count,post in enumerate(posts):
	#	post_lists.append("No.{}:".format(str(count+1)) + str(post)+"<br>")
	#	post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")
	#return HttpResponse(post_lists)
	return HttpResponse(html)


def showpost(request, slug):
	template = get_template('post.html')
	try:
		post =Post.objects.get(slug=slug)
		if post !=None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')

