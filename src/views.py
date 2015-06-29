from django.shortcuts import render
import datetime
# Create your views here.

from src.models import Interior_Designer
from src.models import Electrician
from src.models import Plumber
from src.models import Carpainter
from src.models import Painter
from src.models import Mechanic

def helpers(request):
	now = datetime.datetime.now()   
	tmrw = datetime.date.today() + datetime.timedelta(days = 1)
	tmrw_day = str(tmrw.strftime("%d"))
	
	Intr_Desi_today = Interior_Designer.objects.filter(helper_date__day = now.strftime("%d"))
	Intr_Desi_tmrw = Interior_Designer.objects.filter(helper_date__day = tmrw_day)
	Intr_Desi_all = Interior_Designer.objects.all()
	return render(request, 'helpers.html', {'Intr_Desi_all': Intr_Desi_all,'Intr_Desi_today': Intr_Desi_today, 'Intr_Desi_tmrw': Intr_Desi_tmrw})

	carpainter_today = Carpainter.objects.filter(helper_date__day = now.strftime("%d"))
	carpainter_tmrw = Carpainter.objects.filter(helper_date__day = tmrw_day)
	carpainter_all = Carpainter.objects.all()
	return render(request, 'helpers.html', {'carpainter_all': carpainter_all,'carpainter_today': carpainter_today, 'carpainter_tmrw': carpainter_tmrw})

	painter_today = Painter.objects.filter(helper_date__day = now.strftime("%d"))
	painter_tmrw = Painter.objects.filter(helper_date__day = tmrw_day)
	painter_all = Painter.objects.all()
	return render(request, 'helpers.html', {'painter_all': painter_all,'painter_today': painter_today, 'painter_tmrw': painter_tmrw})

	mech_today = Mechanic.objects.filter(helper_date__day = now.strftime("%d"))
	mech_tmrw = Mechanic.objects.filter(helper_date__day = tmrw_day)
	mech_all = Mechanic.objects.all()
	return render(request, 'helpers.html', {'mech_all': mech_all,'mech_today': mech_today, 'mech_tmrw': mech_tmrw})

	
	elect_today = Electrician.objects.filter(helper_date__day = now.strftime("%d"))
	elect_tmrw = Electrician.objects.filter(helper_date__day = tmrw_day)
	elect_all = Electrician.objects.all()
	return render(request, 'helpers.html', {'elect_all': elect_all,'elect_today':elect_today, 'elect_tmrw':elect_tmrw})
	
	plumber_today = Plumber.objects.filter(helper_date__day = now.strftime("%d"))
	plumber_tmrw = Plumber.objects.filter(helper_date__day = tmrw_day)
	plumber_all = Plumber.objects.all()
	return render(request, 'helpers.html', {'plumber_all': plumber_all,'plumber_today': plumber_today, 'plumber_tmrw': plumber_tmrw})


def helpers_info(request, helpers_id):

	info_helpers = Interior_Designer.objects.get(pk = helpers_id)
	info_helpers = Electrician.objects.get(pk = helpers_id) #getting the perticular object
	info_helpers = Plumber.objects.get(pk = helpers_id)
	info_helpers = Carpainter.objects.get(pk = helpers_id)
	info_helpers = Painter.objects.get(pk = helpers_id)
	info_helpers = Mechanic.objects.get(pk = helpers_id)
	
	return render(request, 'helpers_info.html',{'info_helpers': info_helpers})