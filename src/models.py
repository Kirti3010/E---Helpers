from django.db import models

# Create your models here.
class Interior_Designer(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)

class Electrician(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)

class Plumber(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)

class Carpainter(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)

class Painter(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)

class Mechanic(models.Model):
	Person_name =  models.CharField(max_length = 75)
	Person_phn_no = models.CharField(max_length = 10)
	Person_address = models.CharField(max_length = 300)
	Person_rate = models.IntegerField(default = 0)
	Person_status = models.CharField(max_length = 30)
	Person_date = models.DateField()
	Person_timing = models.TimeField()


	def __str__(self):
		return self.Person_name + " | " + self.Person_address + " | " + str(self.Person_timing) + " | " + str(self.Person_date)
