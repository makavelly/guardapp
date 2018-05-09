from django.db import models

class Employee(models.Model):
	"""
	Model representing a guard in a security company
	"""
	first_name = models.CharField(max_length=100, verbose_name="Имя")
	last_name = models.CharField(max_length=100, verbose_name="Фамилия")
	middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отчество")
	
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
	date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")

	# In order for paginator to work and represent results in some
	# order, we have to set ordering property in Meta class.
	# Another reason is to control the default ordering of records
	# returned when you query the model type
	class Meta:
		ordering = ["last_name", "first_name"]
	
	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return f'{self.last_name}, {self.first_name}'
		
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
	