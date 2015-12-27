from django.contrib import admin

from django import forms
from core.models import *


# Register your models here.



class GoalForm(forms.ModelForm):
    """ """
    class Meta:
        model = Goal
        exclude = [ ]
        # fields = ['short_name','long_desc','user','is_private', ]
        widgets = {
            'short_name':forms.Textarea,
            'long_desc':forms.Textarea
        }

class GoalAdmin(admin.ModelAdmin):
    form = GoalForm
    list_display = ('short_name','long_desc','user','is_private')

admin.site.register(Goal, GoalAdmin)




class EntryForm(forms.ModelForm):
    """ """
    class Meta:
        model = Entry
        # fields = 'int_entry','float_entry','text_entry','pub_date','goal'
        exclude = []
        # widgets = {
        #     'long_name':forms.Textarea,
        #     'long_text':forms.Textarea
        # }

class EntryAdmin(admin.ModelAdmin):
    form = EntryForm
    list_display = ('int_entry','float_entry','text_entry','pub_date','goal')

admin.site.register(Entry, EntryAdmin)




# class ProductForm(forms.ModelForm):
#     """ """
#     class Meta:
#         model = Product
#         widgets = {
#             'long_name':forms.Textarea,
#             'long_text':forms.Textarea
#         }

# class ProductAdmin(admin.ModelAdmin):
#     form = ProductForm
#     list_display = ('short_name','is_active','frontpage','brand','background_and_text_color')

# admin.site.register(Product, ProductAdmin)