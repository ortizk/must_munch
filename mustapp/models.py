from django.db import models

class Options(models.Model):
	city = models.CharField(max_length=20)
	category = models.CharField(max_length=10)
	pricepoint = models.IntegerField()
	restname = models.CharField(max_length=30)
	cuisine = models.CharField(max_length=30)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	website = models.CharField(max_length=100)
	rate = models.IntegerField()
	description = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)

	def __str__(self):
		return self.restname

		# must have users to implement internal rating system
