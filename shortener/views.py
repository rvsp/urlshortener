from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
# Create your views here.

from analytics.models import ClickEvent

from .models import KirrURL
from .forms import SubmitUrlForm

def home_view_FB(request, *args , **kwargs):
	if request.method == 'POST':
		print(request.POST)
		return render(request,"shortener/home.html",{})



class HomeView(View):
	def get(self,request, *args , **kwargs):
		the_form= SubmitUrlForm()
		bg_image='http://thewowstyle.com/wp-content/uploads/2015/01/green-nature-backgrounds.jpeg'
		context={
			"title": "Short.co",
			"form": the_form,
			"bg_image": bg_image
		}
		return render(request,"shortener/home.html", context)


	def post(self,request, *args , **kwargs):
		form= SubmitUrlForm(request.POST)
		context={
			"title": "Short.co",
			"form": form
		}
		template= "shortener/home.html"
		if form.is_valid():
			new_url=form.cleaned_data.get('url')
			obj, created= KirrURL.objects.get_or_create(url=new_url)
			context={
				"object":obj,
				"created":created,
			}
			if created:
				template="shortener/success.html"
			else:
				template="shortener/already-exists.html"
		return render(request,template,context)








'''
in class base method views we have to write explict code for post method
and easier compared to function based views
'''
class URLRedirectView(View): #class based views
	def get(self, request,shortcode=None,  *args, **kwargs):
		qs=KirrURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj=qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
		

	def post(self, request, *args, **kwargs):
		return HttpResponse()































'''

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):  #function based views
	
	obj= get_object_or_404(KirrURL, shortcode=shortcode)
	#obj_url=obj.url
	print(request.method)
	#try:
	#	obj=KirrURL.objects.get(shortcode=shortcode)
	#except:
	#	obj=KirrURL.objects.all().first()
	
	#obj_url=None
	#qs = KirrURL.objects.filter(shortcode__iexact = shortcode.upper()) #correct method 
	#if qs.exists() and qs.count()==1:
	#	obj=qs.first()
	#	obj_url=obj.url

	return HttpResponse("hello {sc}".format(sc=obj.url))

'''