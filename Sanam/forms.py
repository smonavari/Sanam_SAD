__author__ = 'smonavari'
from django import forms
from .models import *
from django.forms.models import inlineformset_factory


class TicketModelForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = ['title', 'price', 'location', 'time']
        labels = {
            'title':'عنوان',
            'price': 'قیمت',
            'location': 'مکان',
            'time': 'زمان',
        }


class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'address','category', 'subcategory', 'endDate', 'startTime',
                  'seller','EventImage', 'dscp']
        labels = {
            'title': 'عنوان',
            'address': 'آدرس',
            'category':'دسته',
            'subcategory': 'زیر دسته',
            'EventImage': 'عکس رویداد',
            'endDate': 'تاریخ پایان',
            'startTime': 'تاریخ شروع',
            'seller': 'فروشنده',
            'dscp': 'توضیحات',

        }
        widgets = {
            'dscp': forms.Textarea(attrs={'rows': 4, 'maxlength': 255,
                                          'placeholder': 'توضیحات بیشتر :)'}),
            'endDate': forms.TextInput(
                attrs={'id': 'date_input', 'placeholder': '2015-3-8', 'type': 'DateField'}),
            'startTime': forms.TextInput(
                attrs={'id': 'date_input_2', 'placeholder': '2015-3-8 20:14', 'type': 'DateField'}),
            'address': forms.TextInput(attrs={'placeholder': 'لطفا آدرس دقیق را وارد کنید'}),
            'title': forms.TextInput(attrs={'placeholder': 'نه خیلی کلی ! نه خیلی جزئی'}),
            'pk':forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EventModelForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['seller'].required = False


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'عنوان دسته',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام دسته'}),
        }


class SubCategoryModelForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'superCategory']
        labels = {
            'name': 'عنوان زیردسته',
            'superCategory': 'دسته',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'عنوان زیر دسته'}),
        }

        def __init__(self, subcategory, *args, **kwargs):
            self.subcategory = subcategory
            super(SubCategoryModelForm, self).__init__(*args, **kwargs)
            self.fields['name'].initial = subcategory.name
            self.fields['superCategory'].initial = subcategory.superCategory


TicketFormSet = inlineformset_factory(Event, TicketType, fields=('title','location', 'price', 'capacity', 'time'), extra=1,
                                      widgets={'location': forms.TextInput(attrs={'placeholder': 'مکان'}),
                                               'title': forms.TextInput(attrs={'placeholder': 'عنوان'}),
                                               'price': forms.TextInput(attrs={'placeholder': 'قیمت'}),
                                               'capacity': forms.TextInput(attrs={'placeholder': 'ظرفیت'}),
                                               'time': forms.TextInput(attrs={'type': 'DateField', 'placeholder': 'تاریخ برگزاری'}),

                                      })


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields=['gender','photo']

