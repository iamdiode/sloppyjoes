from django.shortcuts import render
from .models import Slide, SlideArea, Category, Location
from .forms import FranchiseForm, FeedbackForm


def index(request):
	bannerarea = SlideArea.objects.filter(active=True, slug='slideshow')
	offerarea = SlideArea.objects.filter(active=True, slug='offers')
	slides = Slide.objects.filter(active=True, slidearea=bannerarea)
	offers = Slide.objects.filter(active=True, slidearea=offerarea)
	categories = Category.objects.filter(active=True)
	context = {"slides": slides, "offers": offers, "categories": categories}
	template = "content/index.html"
	return render(request, template, context)

def menu(request, slug=None):
	if slug is None:
		slug = 'burgers'
	categories = Category.objects.filter(active=True)
	context = {"categories": categories, "slug": slug}
	template = "content/menu.html"
	return render(request, template, context)

def franchise(request):
	message = ""
	error = False
	if request.method == "POST":
		form = FranchiseForm(request.POST)
		if form.is_valid():
			form.save()
			message = "Your request submitted successfully"
		else:
			message = "Something went wrong. Please try again"
			error = True
	categories = Category.objects.filter(active=True)
	context = {"categories": categories, "message": message, "error": error}
	template = "content/franchise.html"
	return render(request, template, context)	

def feedback(request):
	message = ""
	error = False
	if request.method == "POST":
		form = FeedbackForm(request.POST)	
		if form.is_valid():
			form.save()
			message = "Your message received successfully"
		else:
			message = "Something went wrong. Please try again"
			error = True
	categories = Category.objects.filter(active=True)
	locations = Location.objects.filter(active=True)
	context = {"categories": categories, "message": message, "error": error, "locations": locations}
	template = "content/feedback.html"
	return render(request, template, context)