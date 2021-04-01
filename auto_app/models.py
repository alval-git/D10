from django.db import models

# Create your models here.
class Car(models.Model):
	brend = models.CharField(max_length=255)
	car_model = models.CharField(max_length=255)
	release_year = models.IntegerField()
	gearbox_choices = ((0, 'ручная'),(1, 'автомат'),(2, 'робот'),)
	gearbox = models.SmallIntegerField(default=0,choices=gearbox_choices)
	body_color = models.CharField(max_length=255)

	def __str__(self):
		return "{} {}".format(self.brend,self.car_model)
