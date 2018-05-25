from django.shortcuts import render
# replace Django ListView with our own ListView
#from django.views.generic import ListView
#from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .my_lib.views import ListView
from .my_lib.views import DetailView
from .models import Employee
from .models import PageContent
from django.forms.models import model_to_dict
from django.forms import modelform_factory
from django import forms

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

class EmployeeDetailView(DetailView):
	"""
	Details of a specific guard
	By default generic.DetailView loads the results of a query to
	a template located in:
	/application_name/templates/application_name/the_model_name_detail.html
	in our case:
	/staff/templates/staff/employee_detail.html
	"""
	model = Employee
	
class EmployeeCreateView(CreateView):
    """
	Create a guard
	By default generic.CreateView loads the results of a query to
	a template located in:
	/application_name/templates/application_name/the_model_name_form.html
	in our case:
	/staff/templates/staff/employee_form.html
    Changing attribute 'template_name_suffix' to '_create_form'
    would cause the default template_name to be
    /staff/templates/staff/employee_create_form.html
	"""
    model = Employee
    fields = '__all__'
    template_name_suffix = '_create_form';
    
class EmployeeUpdateView(UpdateView):
    """
	Update a guard
	By default generic.UpdateView loads the results of a query to
	a template located in:
	/application_name/templates/application_name/the_model_name_form.html
	in our case:
	/staff/templates/staff/employee_form.html
    Changing attribute 'template_name_suffix' to '_update_form'
    would cause the default template_name to be
    /staff/templates/staff/employee_update_form.html
	"""
    model = Employee
    #fields = '__all__'
    
    template_name_suffix = '_update_form'
    form_class = modelform_factory(
                                   Employee,
                                   fields = '__all__',
                                   error_messages={'date_of_birth':{'invalid':'Пожалуйста, укажите дату в формате дд.мм.гггг, например: 01.01.1970'}},
                                   # Used widgets to set a date format, now format is set via DATE_INPUT_FORMATS in settings.py
                                   #widgets= {
                                   #          'date_of_birth':forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control'}),
                                   #          'passport_issue_date':forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control'}),
                                   #         }
                                  )
    '''
    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(EmployeeUpdateView, self).get_initial()
        #initial['date_of_birth'] = '123'
        return initial
    '''
    