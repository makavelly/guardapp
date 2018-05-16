from django.shortcuts import render
# replace Django ListView with our own ListView
#from django.views.generic import ListView
from .my_lib.views import ListView
from .models import Employee
from .models import PageContent
from django.forms.models import model_to_dict


def index(request):
	"""
	View function for home page of site.
	"""
	# Get number of client's visits and set it to 1 if 'num_visits' key doesn't exist
	num_visits = request.session.get('num_visits', 1)
	request.session['num_visits'] = num_visits + 1
	
	# Get welcome text from a home_page instance of a PageContent model
	# SomeModel.objects.filter(name='home_page').first() instead of get()
	# because filter().first() doesn't fail if instance doesn't exist, it returns None
	welcome_text = 'Текст приветствия не найден'
	home_page = PageContent.objects.filter(name='home_page').first()
	# if page content is found
	if home_page:
		welcome_text = home_page.welcome_text
	
	# Render the HTML template index.html with the data in the context variable
	context = {
		'num_visits': num_visits,
		'welcome_text': welcome_text,
	}
	return render(request, 'staff/home_page.html', context)
	
class EmployeeListView(ListView):
	"""
	List of all guards in a company
	By default generic.ListView loads the results of a query to
	a template located in:
	/application_name/templates/application_name/the_model_name_list.html
	in our case:
	/staff/templates/staff/employee_list.html
	"""
	model = Employee
