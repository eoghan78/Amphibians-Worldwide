
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


#User Registration Form associated with auth.User
class User_Registration_Form(UserCreationForm):
	email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'input is-success is-rounded'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input is-success is-rounded'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input is-success is-rounded'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(User_Registration_Form, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'input is-success is-rounded'
		self.fields['password1'].widget.attrs['class'] = 'input is-success is-rounded'
		self.fields['password2'].widget.attrs['class'] = 'input is-success is-rounded'

#User Profile Form Associated with User_Profile to extend auth.User via One-to-One Relationship
class User_Profile_Form(forms.ModelForm):
	class Meta:
		model = User_Profile
		fields = ('profile_image', 'educational_institution', 'bio', 'university_profile', 'linked_in', 'academia_publication', 'publication_1', 'publication_2', 'publication_3', 'publication_4', 'publication_5', 'permission_to_display_contact_information', 'permission_to_display_publications')

		labels ={
				'profile_image': 'Profile Image', 
		}
	
		widgets = {
		'educational_institution' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'bio' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'university_profile' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'linked_in' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'academia_publication' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'publication_1' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'publication_2' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'publication_3' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'publication_4' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'publication_5' : forms.TextInput(attrs={'class':'input input is-success is-rounded'}),
		'permission_to_display_contact_information' : forms.CheckboxInput(attrs={'class':'checkbox'}),
		'permission_to_display_publications' : forms.CheckboxInput(attrs={'class':'checkbox'}),
		}

#Form to submit data to Species table and one-to-many relationships
class Submit_Species_Form(forms.ModelForm):

	class Meta:
		model = Species
		fields = ('species_name_common', 'species_name_latin', 'size_max_male', 'size_max_female', 'size_max_record', 'longevity', 'clutch_min', 'clutch_max', 'clutch_avg', 'egg_diameter', 'range_size', 'elevation_min', 'elevation_max', 'elevation_avg', 'img_uri_male', 'img_uri_female', 'parity_mode', 'pop_trend', 'iucn', 'genus')
		
		labels ={
				'img_uri_male': 'Male Image', 
				'img_uri_female': 'Female Image',
		}

		widgets = {
		'species_name_common' : forms.TextInput(attrs={'class':'input is-success is-rounded'}),
		'species_name_latin' : forms.TextInput(attrs={'class':'input is-success is-rounded'}),
		'size_max_male' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'size_max_female' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'size_max_record' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'longevity' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'clutch_min' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'clutch_max' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'clutch_avg' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'egg_diameter' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'range_size' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'elevation_min' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'elevation_max' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'elevation_avg' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		'parity_mode' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
		'pop_trend' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
		'iucn' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
		'genus' : forms.Select(attrs={'class':'input is-danger is-rounded'})
		}

#Forms for Many-to-many relations
# class Submit_Species_Form_Continent(forms.ModelForm):

# 	class Meta:
# 		model = Country
# 		fields = ('continent',)

# 		widgets = {'continent' : forms.Select(attrs={'class':'input is-danger is-rounded'}),}


# class Submit_Species_Form_Country_Geo_Location(forms.ModelForm):

# 	class Meta:
# 		model = Geo_Location
# 		fields = ('country', 'region_name', 'latitude', 'longitude')

# 		widgets = {
# 			'country' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
# 			'region_name' : forms.TextInput(attrs={'class':'input is-success is-rounded'}),
# 			'latitude' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
# 			'longitude' : forms.NumberInput(attrs={'class':'input is-info is-rounded'}),
		
# 		}

# class Submit_Species_Form_Order(forms.ModelForm):

# 	class Meta:
# 		model = Family
# 		fields = ('order',)

# 		widgets = {'order' : forms.Select(attrs={'class':'input is-danger is-rounded'}),}

# class Submit_Species_Form_Family(forms.ModelForm):

# 	class Meta:
# 		model = Genus
# 		fields = ('family',)

# 		widgets = {'family' : forms.Select(attrs={'class':'input is-danger is-rounded'}),}

# class Submit_Species_Form_Nesting_Site(forms.ModelForm):

# 	class Meta:
# 		model = Nesting_Site_Species
# 		fields = ('nesting_site',)

# 		widgets = {
# 			'nesting_site' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
# 		}

# class Submit_Species_Form_Activity(forms.ModelForm):

# 	class Meta:
# 		model = Activity_Species
# 		fields = ('activity',)

# 		widgets = {
# 			'activity' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
# 		}


# class Submit_Species_Form_Micro_Habitat(forms.ModelForm):

# 	class Meta:
# 		model = Micro_Habitat_Species
# 		fields = ('micro_habitat', 'species')

# 		widgets = {
# 			'micro_habitat' : forms.Select(attrs={'class':'input is-danger is-rounded'}),
# 			'species' : forms.HiddenInput(),		
# 		}

#Approving a Species Submission to Make Viewable on the Website
class Approve_Species_Form(forms.ModelForm):
	class Meta:
		model = Species
		fields = ('verif_status',)
	
		widgets = {
		'verif_status' : forms.CheckboxInput(attrs={'class':'checkbox'}),
		
		}

