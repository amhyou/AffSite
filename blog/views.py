from django.shortcuts import render,redirect
from .models import *
from django.forms import ModelForm
from django.contrib import messages

def index(request):
	logoni = Aboutme.objects.all()[0]

	arts = Article.objects.order_by('?')
	topics = Topic.objects.all()
	fit = Article.objects.order_by('?')
	wirea = fit[0]
	trend = fit[1]

	fit2 = Banner.objects.order_by('?')
	wirea2 = fit2[:len(fit2)//2]
	trend2 = fit2[len(fit2)//2:]

	cntx = {"logoni":logoni,"arts":arts,"topics":topics,"wirea":wirea,"trend":trend,"zid1":wirea2,"zid2":trend2}
	return render(request,"index.html",cntx)


def topic(request,topic):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	element = Topic.objects.filter(name=topic)
	arts = Article.objects.filter(subject__name=topic)
	fit = Article.objects.order_by('?')
	wirea = fit[0] 
	trend = fit[1]

	fit2 = Banner.objects.order_by('?')
	wirea2 = fit2[:len(fit2)//2]
	trend2 = fit2[len(fit2)//2:]

	cntx = {"logoni":logoni,"arts":arts,"topics":topics,"wirea":wirea,"trend":trend,"zid1":wirea2,"zid2":trend2}
	if element:
		return render(request,"index.html",cntx)
	return redirect("/")
	


def article(request,topic,idd):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	fit = Article.objects.order_by('?')
	wirea = fit[0] 
	trend = fit[1]

	arts = Article.objects.filter(subject__name=topic).order_by('?')
	next_art = arts[0]
	rel_arts = arts[1:]

	fit2 = Banner.objects.order_by('?')
	wirea2 = fit2[:len(fit2)//2]
	trend2 = fit2[len(fit2)//2:]

	cntx = {"logoni":logoni,"art":Article.objects.get(pk=idd),"topics":topics,"nowtopic":topic,
	"wirea":wirea,"trend":trend,"nexta":next_art,"relar":rel_arts,
	"zid1":wirea2,"zid2":trend2}
	return render(request,"article.html",cntx)


def about(request):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	aboutme = Aboutme.objects.all()[0]
	cntx = {"logoni":logoni,"topics":topics,"infos":aboutme}
	return render(request,"infos/about.html",cntx)

class Textme(ModelForm):
	class Meta:
		model = MSG
		fields = '__all__'

def contact(request):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	if request.method=="POST":
		form2 = Textme(request.POST)
		if form2.is_valid():
			form2.save()
			messages.success(request, 'Your message has been successfully sent')
	form = Textme()
	cntx = {"logoni":logoni,"topics":topics,"form":form}
	return render(request,"infos/contact.html",cntx)


def terms(request):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	cntx = {"logoni":logoni,"topics":topics}
	return render(request,"infos/terms.html",cntx)

def privacy(request):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	cntx = {"logoni":logoni,"topics":topics}
	return render(request,"infos/privacy.html",cntx)

def copyright(request):
	logoni = Aboutme.objects.all()[0]

	topics = Topic.objects.all()
	cntx = {"logoni":logoni,"topics":topics}
	return render(request,"infos/copyright.html",cntx)
