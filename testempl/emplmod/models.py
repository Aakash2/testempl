from django.db import models 

# Create your models here.
from django import forms
from django.forms import ModelForm
from django.forms import CharField,Textarea, MultipleChoiceField,ChoiceField,Select,RadioSelect,ModelChoiceField,DecimalField,DateTimeField,IntegerField,DateField,TextInput

class Departments(models.Model):
	dept_id=models.AutoField(primary_key=True)
	dept_name=models.CharField(blank=True,max_length=15)
	dept_deleted=models.CharField(max_length=1)
	
	def __unicode__(self):
        	return self.dept_name

class Employee_Details(models.Model):
	empl_id= models.AutoField(primary_key=True)
	empl_fullname=models.CharField(blank=False,max_length=25)
	empl_dob= models.DateField(max_length=15, null=False,blank=False)
	empl_address=models.TextField(blank=False,max_length=50)
	empl_joiningdate=models.DateTimeField(auto_now_add=True,null=False,blank=False)
	empl_designation=models.CharField(blank=False,max_length=25)
	empl_dept_id=models.ForeignKey('Departments',related_name='empl_dept_id-dept_id',null=True,blank=False)
	empl_email=models.CharField(blank=False,max_length=20)
	empl_gender=models.CharField(blank=False,max_length=6)
	empl_phoneno=models.CharField(blank=False,max_length=10)
	empl_deleted=models.CharField(blank=False,max_length=1)
	empl_created=models.DateTimeField(auto_now_add=True,null=False,blank=False)

class Employee_Details_form(forms.ModelForm):
	empl_fullname=forms.CharField(label='Full Name',max_length=25)
	empl_dob= forms.DateField(widget=forms.TextInput(attrs={'class':'required text'}),input_formats=["%d/%m/%Y"],label='DOB')
	empl_address=forms.CharField(widget=forms.Textarea(attrs={'rows':'6','cols':'40','class':'text multitext'}))
	empl_designation=forms.CharField(label='Designation',max_length=25)
	empl_joiningdate=empl_dob= forms.DateField(widget=forms.TextInput(attrs={'class':'required text'}),input_formats=["%d/%m/%Y"],label='Joining Date')
	empl_dept_id=forms.ModelChoiceField(queryset=Departments.objects.filter(dept_deleted='N'),empty_label='Select',widget=Select(attrs={'class':'text','style':'width:212px;height:30px;margin:5px 0 5px 0;'}))
	empl_email=forms.CharField(label='Email ID',max_length=20)
	empl_gender=forms.CharField(label='Gender',max_length=6)
	empl_phoneno=forms.CharField(label='Contact Number',max_length=10)
	class Meta:
		model=Employee_Details
		exclude=('empl_deleted','empl_created')
