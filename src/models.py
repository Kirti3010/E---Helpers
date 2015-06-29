from django.db import models

# Create your models here.
class Helpers(models.Model):

	class Electrician_Helpers(models.Model):
		helper_name =  models.CharField(max_length = 75)
		helper_phn_no = models.CharField(max_length = 10)
		helper_address = models.CharField(max_length = 300)
		helper_rate = models.IntegerField(default = 0)
		helper_status = models.CharField(max_length = 30)
		helper_date = models.DateField()
		helper_timing = models.TimeField()


		def __str__(self):
			return self.helper_name + " | " + self.helper_address + " | " + str(self.helper_timing) + " | " + str(self.helper_date)
