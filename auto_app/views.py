from django.shortcuts import render
from auto_app.models import Car
from django.views.generic import ListView, TemplateView
from django.db.models import Q
# Create your views here.
class CarListView(TemplateView):
	template_name = 'index.html'
	model = Car
	context_object_name = 'cars'
	# def get_queryset(self):
	# 	input_query = self.request.GET.get('q','')
	# 	search_list = input_query.split()
	# 	transmission = -1
	# 	int_search_list = []
	# 	for item in search_list:
	# 		if item.isdigit():
	# 			int_search_list.append(int(item))
	# 	if ("ручная" in search_list):
	# 		transmission = 0
	# 	if ("автомат" in search_list):
	# 		transmission = 1
	# 	if ("робот" in search_list):
	# 		transmission = 2
 #        # search
	# 	if input_query:
	# 		filter_cars = Car.objects.filter(Q(brend__in=search_list) |
	# 									  Q(car_model__in=search_list) |
	# 									  Q(body_color__in=search_list) |
	# 									  Q(gearbox= transmission) |
	# 									  Q(release_year__in= int_search_list)
	# 									) 
	# 		return filter_cars
	# 	else:
	# 		return  Car.objects.all()
	# def get_queryset(self):
	# 	# input_brend = self.request.GET.get('brend')
	# 	# if not input_brend :
	# 	# 	input_brend = ""
	# 	# input_model = self.request.GET.get('model')
	# 	# if not input_brend :
	# 	# 	input_model = ""
	# 	# input_year = self.request.GET.get('year')
	# 	# if not input_brend :
	# 	# 	input_year = ""
	# 	# input_color = self.request.GET.get('color')
	# 	# if not input_brend :
	# 	# 	input_color = ""
	# 	# gearbox_choice = self.request.GET.get('gearbox')
	# 	# if not input_brend :
	# 	# 	gearbox_choice = ""
	# 	# filter_cars = Car.objects.filter(Q(brend__icontains=input_brend) |
	# 	# 								  Q(car_model__icontains =input_model) |
	# 	# 								  Q(body_color__icontains=input_color) 
										  
	# 	# 								) 
	# 	# if (filter_cars):
	# 	# 	return filter_cars
	# 	# else:
	# 	# 	return Car.objects.all()
	def get_context_data(self, **kwargs):
		params = self.request.GET
		query = Q()
		for key, value in params.items():
			if value and key in vars(Car):
				query &= Q(**{key: value})
		print(query)
		return {"cars": Car.objects.filter(query)}