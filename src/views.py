from django.shortcuts import render
import datetime
# Create your views here.

from src.models import Helpers 

def helpers(request):
	now = datetime.datetime.now()   
	tmrw = datetime.date.today() + datetime.timedelta(days = 1)
	tmrw_day = str(tmrw.strftime("%d"))
	
	helpers_today = Helpers.objects.filter(helper_date__day = now.strftime("%d"))
	helpers_tmrw = Helpers.objects.filter(helper_date__day = tmrw_day)
	helpers_all = Helpers.objects.all()
	return render(request, 'helpers.html', {'helpers_all': helpers_all,'helpers_today':helpers_today, 'helpers_tmrw':helpers_tmrw})

def helpers_info(request, helpers_id):
	info_helpers = Helpers.objects.get(pk = helpers_id) #getting the perticular object

	return render(request, 'helpers_info.html',{'info_helpers': info_helpers})