from django.db import models

# Create your models here.

#Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    
    def __unicode__(self):
    	return self.name


#Food

class Food(models.Model):
	name = models.CharField(max_length=40)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	comment = models.CharField(max_length=60)
	is_spicy = models.BooleanField(default = False)
	restaurant = models.ForeignKey(Restaurant)

	def __unicode__(self):
		return self.name