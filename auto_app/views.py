from django.shortcuts import render
from auto_app.models import Car
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.
class CarListView(ListView):
	template_name = 'index.html'
	model = Car
	context_object_name = 'cars'
	def get_queryset(self):
		input_query = self.request.GET.get('q','')
		search_list = input_query.split()
		transmission = -1
		int_search_list = []
		for item in search_list:
			if item.isdigit():
				int_search_list.append(int(item))
		if ("ручная" in search_list):
			transmission = 0
		if ("автомат" in search_list):
			transmission = 1
		if ("робот" in search_list):
			transmission = 2
        # search
		if input_query:
			filter_cars = Car.objects.filter(Q(brend__in=search_list) |
										  Q(car_model__in=search_list) |
										  Q(body_color__in=search_list) |
										  Q(gearbox= transmission) |
										  Q(release_year__in= int_search_list)
										) 
			return filter_cars
		else:
			return  Car.objects.all()
