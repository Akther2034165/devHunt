from django.forms import  ModelForm, TextInput, FileInput, Textarea
from .models import Project, Review, Tag
from django import forms
class ProjectForm(ModelForm):
   
    class Meta:
        model = Project 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'border py-2 border-1 mt-1 block w-full rounded-md border-gray-300 shadow-sm ', 'placeholder' : ' write title'})
        self.fields['description'].widget.attrs.update({'class': 'border py-2 border-1 mt-1 block w-full rounded-md border-gray-300 shadow-sm resize-none h-[115px]'})
        self.fields['featured_image'].widget.attrs.update({'class': 'file-input w-full'})
        self.fields['demo_link'].widget.attrs.update({'class': 'border py-2 border-1 mt-1 rounded-md border-gray-300 shadow-sm w-full'})
        self.fields['source_link'].widget.attrs.update({'class': 'border py-2 border-1 mt-1 rounded-md border-gray-300 shadow-sm w-full'})
        self.fields['tags'].widget.attrs.update({'class': 'border py-2 border-1 mt-1   rounded-md border-gray-300 shadow-sm p-2'})
        