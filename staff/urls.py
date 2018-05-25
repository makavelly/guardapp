from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
	path('', views.index, name='index'),
	path('employee_list/', views.EmployeeListView.as_view(), name='employees'),
	path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
	path('employee/create', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee-update'),
]

