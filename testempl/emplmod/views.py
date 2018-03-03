from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import emplmod
from emplmod.models import Employee_Details_form
from django.template import RequestContext

def loginauth(request):
	response=HttpResponse()
	if request.method == 'GET':
		fobj=Employee_Details_form()
		return render_to_response('html/addempdet.htm',{'pForm':fobj.as_table()},context_instance=RequestContext(request)) 
