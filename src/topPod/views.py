# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Sport, Pod
from django.views.generic import TemplateView

class Home(TemplateView):
	template_name = 'home.html'
	
	def get_context_data(self):
		context = super(Home, self).get_context_data()
		query = self.request.GET.get('query')
		context['sports'] = Sport.objects.all()

		return context

class Sports(TemplateView):
	template_name = 'sport.html'

	def get_context_data(self, *args, **kwargs):
		context = super(Sports, self).get_context_data()
		query = self.request.GET.get('query')
		selected_sport 		= Sport.objects.get(slug=self.kwargs['slug'])
		context['sports'] 	= Sport.objects.all()
		context['category'] = Sport.objects.get(slug=self.kwargs['slug'])
		context['pods']		= Pod.objects.filter(sport_id = selected_sport.id)
		if query:
			context['pods'] = Pod.objects.filter(name__icontains=query)
		return context

class AllPods(TemplateView):
	template_name = 'pods.html'

	def get_context_data(self, *args, **kwargs):
		context = super(AllPods, self).get_context_data()
		query = self.request.GET.get('query')
		context['sports'] 	= Sport.objects.all()
		if query:
			context['pods'] = Pod.objects.filter(name__icontains=query)
		return context