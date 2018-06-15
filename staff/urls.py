from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
	path('', views.index, name='index'),
	path('employee_list/', views.EmployeeListView.as_view(), name='employees'),
	path('employee/<int:pk>', views.EmployeeDetailView.as_view(), name='employee-detail'),
	path('employee/create', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update', views.EmployeeUpdateView.as_view(), name='employee-update'),
    
    path('chief_list/', views.ChiefListView.as_view(), name='chiefs'),
    path('chief/<int:pk>', views.ChiefDetailView.as_view(), name='chief-detail'),
	path('chief/create', views.ChiefCreateView.as_view(), name='chief-create'),
    path('chief/<int:pk>/update', views.ChiefUpdateView.as_view(), name='chief-update'),
]

