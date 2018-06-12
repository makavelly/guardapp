from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Person(models.Model):
    """
    Model representing a person
    todo: translation into English
    """
    # Some rules for model fields
    # blank=True - the field on the site page could be left blank, is not required
    # null=True allows the database to store a Null value if the field left blank

    # Required fields
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    #middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
    middle_name = models.CharField(max_length=100, blank=True, null=False, default = "", verbose_name="Отчество")

    # todo - enter a phone number via regex and country code
    phone_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер телефона")

    passport_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер паспорта")
    passport_issue_date = models.DateField(blank=True, null=True, verbose_name="Когда выдан паспорт")
    passport_issued_by = models.CharField(max_length=100, blank=True, null=True, verbose_name="Кем выдан паспорт")

    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
    street = models.CharField(max_length=100, blank=True, null=True, verbose_name="Улица")
    building = models.CharField(max_length=100, blank=True, null=True, verbose_name="Дом")
    wing = models.CharField(max_length=100, blank=True, null=True, verbose_name="Корпус")
    apartment = models.CharField(max_length=100, blank=True, null=True, verbose_name="Квартира")

    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения", error_messages={'invalid': 'this field is invalid'})

    license_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер удостоверения")
    license_valid_thru = models.DateField(blank=True, null=True, verbose_name="Удостоверение действительно до")
    # Abstract base classes are useful when you want to
    # put some common information into a number of other models.
    # You write your base class and put abstract=True in the Meta class.
    # This model will then not be used to create any database table.
    # Instead, when it is used as a base class for other models,
    # its fields will be added to those of the child class.
    class Meta:
        abstract = True
        # In order for paginator to work and represent results in some
        # order, we have to set ordering property in Meta class.
        # Another reason is to control the default ordering of records
        # returned when you query the model type
        ordering = ["last_name", "first_name"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'{self.last_name}, {self.first_name}'
        
class Guard(Person):
    """
    A Guard is a Person with a special license
    """
    license_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер удостоверения")
    license_valid_thru = models.DateField(blank=True, null=True, verbose_name="Удостоверение действительно до")
    # If the child wants to extend the parent’s Meta class, it can subclass it
    class Meta(Person.Meta):
        abstract = True
        
    
    
class Employee(Guard):
    """
    Model representing a guard in a security company
    """
    # If a child class does not declare its own Meta class,
    # it will inherit the parent’s Meta.
    #class Meta:
    #    ordering = ["last_name", "first_name"]
	
    chief = models.ForeignKey('Chief', on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        """
        #Returns the url to access a detail record for this empolyee.
        """
        return reverse('employee-detail', args=[str(self.id)])
	
    def	dict_of_fields_and_values(self):
        return {getattr(self,k):v for (k, v) in self.__dict__.items() if not k.startswith('_') and not callable(k)}

class Chief(Guard):
    """
    Model representing a chief of guards in a security company
    """
    # If a child class does not declare its own Meta class,
    # it will inherit the parent’s Meta.
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this chief.
        """
        return reverse('chief-detail', args=[str(self.id)])
    
"""
class Employee(models.Model):
"""
	#Model representing a guard in a security company
"""
	first_name = models.CharField(max_length=100, verbose_name="Имя")
	last_name = models.CharField(max_length=100, verbose_name="Фамилия")
	#middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
	middle_name = models.CharField(max_length=100, blank=True, null=False, default = "", verbose_name="Отчество")
	
	phone_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер телефона")
	
	passport_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер паспорта")
	passport_issue_date = models.DateField(blank=True, null=True, verbose_name="Когда выдан паспорт")
	passport_issued_by = models.CharField(max_length=100, blank=True, null=True, verbose_name="Кем выдан паспорт")
	
	city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Город")
	street = models.CharField(max_length=100, blank=True, null=True, verbose_name="Улица")
	building = models.CharField(max_length=100, blank=True, null=True, verbose_name="Дом")
	wing = models.CharField(max_length=100, blank=True, null=True, verbose_name="Корпус")
	apartment = models.CharField(max_length=100, blank=True, null=True, verbose_name="Квартира")
	# blank=True - the field on the site page could be left blank, is not required
	# null=True allows the database to store a Null value if the field left blank
	date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения", error_messages={'invalid': 'this field is invalid'})

	license_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Номер удостоверения")
	license_valid_thru = models.DateField(blank=True, null=True, verbose_name="Удостоверение действительно до")
	# In order for paginator to work and represent results in some
	# order, we have to set ordering property in Meta class.
	# Another reason is to control the default ordering of records
	# returned when you query the model type
	class Meta:
		ordering = ["last_name", "first_name"]
	
	def __str__(self):
"""
		#String for representing the Model object.
"""
		return f'{self.last_name}, {self.first_name}'
		
	def get_absolute_url(self):
"""
		#Returns the url to access a detail record for this empolyee.
"""
		return reverse('employee-detail', args=[str(self.id)])
	
	def	dict_of_fields_and_values(self):
		return {getattr(self,k):v for (k, v) in self.__dict__.items() if not k.startswith('_') and not callable(k)}
"""

class PageContent(models.Model):
	"""
	Model representing some text fields on a page.
	In order to manage content of a page from an admin site.
	"""
	name = models.CharField(max_length=100)
	welcome_text = models.TextField(blank=True, null=True)
	main_text = models.TextField(blank=True, null=True)
	additional_text = models.TextField(blank=True, null=True)
	help_text = models.TextField(blank=True, null=True)
	