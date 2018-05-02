from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from eventfoldersrc.models import Venue, Catering, LightsAndSounds

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)

class VenuesPageView(TemplateView):
	def get(self, request, **kwargs):
		venues_list = Venue.objects.order_by('name')
		context = {'venues_list': venues_list}
		return render(request, 'venues.html', context)

class CateringsPageView(TemplateView):
	def get(self, request, **kwargs):
		caterings_list = Catering.objects.order_by('name')
		context = {'caterings_list': caterings_list}
		return render(request, 'caterings.html', context)

class LightsAndSoundsPageView(TemplateView):
	def get(self, request, **kwargs):
		lightssounds_list = LightsAndSounds.objects.order_by('name')
		context = {'lightssounds_list': lightssounds_list}
		return render(request, 'lightssounds.html', context)