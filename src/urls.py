from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.helpers, name = 'helpers'),
	url(r'^(?P<helpers_id>\d+)/$',views.helpers_info, name = 'helpers_info')
]