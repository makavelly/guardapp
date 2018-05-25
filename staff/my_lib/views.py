from django.views.generic import ListView as DjangoListView
from django.views.generic import DetailView as DjangoDetailView
 
class ListView(DjangoListView):
    '''
    Enhanced ListView which also includes the ``model`` in the context data,
    so that the template has access to its model class.
    '''
 
    def get_context_data(self):
        '''
        Adds the model to the context data.
        '''
        context = super(ListView, self).get_context_data()
        #field_list = [field for field in self.model._meta.get_fields() if field.name != 'id']
        field_list = self.model._meta.get_fields()
        context['field_list'] = field_list
        #context['field_list'] = self.model._meta.get_fields(include_hidden=False)
        return context
		
class DetailView(DjangoDetailView):
    '''
    Enhanced DetailView which also includes the ``model`` in the context data,
    so that the template has access to its model class.
    '''
    
    def fields(self):
        return {field.verbose_name: field for field in self.model._meta.get_fields()}
        #for field in self.model._meta.get_fields():
        #    {field.verbose_name: "1" for field in self.model._meta.get_fields()}
        #return self.model._meta.get_fields()
		
    '''def get_context_data(self):
        # Adds the model to the context data.
        context = super(DetailView, self).get_context_data()
        #field_list = [field for field in self.model._meta.get_fields() if field.name != 'id']
        field_list = self.model._meta.get_fields()
        context['field_list'] = field_list
        #context['field_list'] = self.model._meta.get_fields(include_hidden=False)
        return context
	'''