from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count

from home.forms import *
from .models import *

#xhtml2pdf imports
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



#Index View
def index_view(request):
    return render(request, 'home/index.html', {})

#Data Summary View
def data_summary_view(request):
    #Taxonomy Breakdown
    num_genus = Genus.objects.all().count()
    num_species = Species.objects.all().count()
    num_families = Family.objects.all().count()
    num_orders = Order_Taxon.objects.all().count()

    #Variable Breakdown
    #Many to Many
    activity_ranking = Activity.objects.all().annotate(count=Count('activity_id')).order_by("-count")
    nesting_site_ranking = Nesting_Site.objects.all().annotate(count=Count('nesting_site_id')).order_by("-count")
    microhabitat_ranking = Micro_Habitat.objects.all().annotate(count=Count('micro_habitat_id')).order_by("-count")

    #One to Many
    parity_mode_ranking = Parity_Mode.objects.all().annotate(count=Count('parity_mode_id')).order_by('-count')
    pop_trend_ranking = Pop_Trend.objects.all().annotate(count=Count('pop_trend_id')).order_by("-count")
    iucn_ranking = IUCN.objects.all().annotate(count=Count('iucn_id')).order_by("-count")
    

    #Geographical Representations 
    continent_ranking = Continent.objects.all().annotate(count=Count('continent_id')).order_by('-count')
    country_ranking = Country.objects.all().annotate(count=Count('country_id')).order_by('-count')

    context = {
        'num_genus':  num_genus,
        'num_species': num_species,
        'num_families': num_families,
        'num_orders': num_orders,
        'activity_ranking': activity_ranking,
        'nesting_site_ranking':  nesting_site_ranking,
        'microhabitat_ranking': microhabitat_ranking,
        'parity_mode_ranking': parity_mode_ranking,
        'pop_trend_ranking': pop_trend_ranking,
        'iucn_ranking': iucn_ranking,
        'continent_ranking': continent_ranking,
        'country_ranking':country_ranking,
      
    
    }
    return render(request, 'home/search/data_summary.html', context)

###################################################PDF Generator#########################################################
def species_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    species = get_object_or_404(Species, pk=pk)

    template_path = 'home/staff/pdf_creator.html'
    context = {'species': species}
    # Creates a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="species.pdf"'
    # finds the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # creates a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



#################################################Nav Bar Views#######################################################

def location_view(request):
    return render(request, 'home/search/location.html')

def loca_continent_view(request):
    continent_list = Continent.objects.all().order_by('continent_name')
    return render (request, 'home/search/loca_continent.html', {'continent_list': continent_list})

def loca_country_view(request):
    country_list = Country.objects.all().order_by('country_name')
    return render (request, 'home/search/loca_country.html', {'country_list': country_list})

def micro_habitat_view(request):
    micro_habitat_list = Micro_Habitat.objects.all().order_by('micro_habitat_name')
    return render(request, 'home/search/micro_habitat.html', {'micro_habitat_list': micro_habitat_list})

def activity_view(request):
    activity_list = Activity.objects.all().order_by('activity_kind')
    return render(request, 'home/search/activity.html', {'activity_list': activity_list})

def population_trend_view(request):
    pop_trend_list = Pop_Trend.objects.all().order_by('pop_trend_status')
    return render(request, 'home/search/population_trend.html', {'pop_trend_list': pop_trend_list})

def iucn_view(request):
     iucn_list = IUCN.objects.all().order_by('iucn_status')
     return render(request, 'home/search/iucn.html', {'iucn_list': iucn_list})

def nesting_site_view(request):
    nesting_site_list = Nesting_Site.objects.all().order_by('nesting_site_desc')
    return render(request, 'home/search/nesting_site.html', {'nesting_site_list': nesting_site_list})

def parity_mode_view(request):
    parity_mode_list = Parity_Mode.objects.all().order_by('parity_mode_desc')
    return render(request, 'home/search/parity_mode.html', {'parity_mode_list': parity_mode_list})

def taxonomy_view(request):
    return render(request, 'home/search/taxonomy.html')

def tax_order_view(request):
    order_taxon_list = Order_Taxon.objects.all().order_by('order_taxon_name')
    return render(request, 'home/search/tax_order.html', {'order_taxon_list': order_taxon_list})


def tax_family_view(request):
    family_list = Family.objects.all().order_by('family_name')
    return render(request, 'home/search/tax_family.html', {'family_list': family_list})


def tax_genus_view(request):
    genus_list = Genus.objects.all().order_by('genus_name')
    return render(request, 'home/search/tax_genus.html', {'genus_list': genus_list})


###############################################Search Views########################################################
  
def search_species_latin_name_view(request):

    if request.method == "POST":
        searched= request.POST['searched']
        species_results = Species.objects.filter(species_name_latin__contains = searched).order_by('species_name_latin' )
        
        return render(request, 'home/search/search_species.html', {'searched':searched, 'species_results':species_results})

    else:
        
        return redirect ('home:index')

    
###############################################Species Views######################################################

class Species_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'

class Species_Detail_Detail_View (DetailView):
    model = Species
    template_name = "home/search/species_detail.html"
    context_object_name = 'species_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order_Taxon.objects.filter(family__genus__genus_id=context['object'].genus_id)
        context['family_list'] = Family.objects.filter(genus__genus_id=context['object'].genus_id)
        context['country_list'] = Country.objects.filter(geo_location__geo_location_species__species_id=context['object'].species_id)
        context['continent_list'] = Continent.objects.filter(country__geo_location__geo_location_species__species_id=context['object'].species_id)

        return context
   

###########################################One to Many Views########################################################

class Species_Parity_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'
    

    def get_queryset(self):
    
        return Species.objects.filter(parity_mode_id=self.kwargs['parity_mode_id']).order_by('species_name_latin')



class Species_Pop_Trend_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'

    def get_queryset(self):
    
        return Species.objects.filter(pop_trend_id=self.kwargs['pop_trend_id']).order_by('species_name_latin')


class Species_Iucn_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
    
        return Species.objects.filter(iucn_id=self.kwargs['iucn_id']).order_by('species_name_latin')



################################################Many to Many Views###################################################

class Species_Nesting_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'
    
    def get_queryset(self): 

        return Species.objects.filter(nesting_site_species__nesting_site__nesting_site_id= self.kwargs['nesting_site_id']).order_by('species_name_latin')

    

class Species_Micro_Habitat_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'

    def get_queryset(self): 

        return Species.objects.filter(micro_habitat_species__micro_habitat__micro_habitat_id= self.kwargs['micro_habitat_id']).order_by('species_name_latin')



class Species_Activity_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self): 
        return Species.objects.filter(activity_species__activity__activity_id= self.kwargs['activity_id']).order_by('species_name_latin').order_by('species_name_latin' )
       

###############################################Hierarchical Views####################################################

class Species_Country_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self): 
        return Species.objects.filter(geo_location_species__geo_location__country_id=self.kwargs['country_id']).order_by('species_name_latin').order_by('species_name_latin' ) 
      

class Species_Continent_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(geo_location_species__geo_location__country__continent__continent_id=self.kwargs['continent_id']).order_by('species_name_latin').order_by('species_name_latin')    
        

class Species_Tax_Order_List_View(ListView):

    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(genus__family__order_id=self.kwargs['order_id']).order_by('species_name_latin').order_by('species_name_latin' )    
        


class Species_Family_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(genus__family_id=self.kwargs['family_id']).order_by('species_name_latin').order_by('species_name_latin' )  
       

class Species_Genus_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/search/species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(genus_id=self.kwargs['genus_id']).order_by('species_name_latin').order_by('species_name_latin')     
        

####################################Sign up and Login/LogoutViews####################################################

  
def login_user_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In")
            return redirect("home:index")
       
        else:
            messages.success(request, "Incorrect username or password")
            return redirect("home:login")
    
    else:
        return render(request, 'registration/login.html', {})

def logout_user_view(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect ('home:index')


def signup_view(request):
   
   if request.method == "POST":
        user_form = User_Registration_Form(request.POST or None)
        user_profile_form = User_Profile_Form(request.POST, request.FILES or None)
        if user_form.is_valid() and user_profile_form.is_valid():
       
            user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('home:index')
   else:
        user_form = User_Registration_Form()
        user_profile_form = User_Profile_Form()
   
   return render(request, 'registration/signup.html',  {"u_form":user_form, "p_form":  user_profile_form})

###############################################User Views############################################################

def my_page_view(request):
    
    return render(request, "home/account/mypage.html", {})


def submit_species_view(request):
        
        species_form = Submit_Species_Form(request.POST or None, request.FILES or None)
        # continent_form = Submit_Species_Form_Continent(request.POST or None)
        # country_form = Submit_Species_Form_Country_Geo_Location(request.POST or None)
        # order_form = Submit_Species_Form_Order(request.POST or None)
        # family_form = Submit_Species_Form_Family(request.POST or None)
        # micro_habitat_form = Submit_Species_Form_Micro_Habitat(request.POST or None)
        # activity_form = Submit_Species_Form_Activity(request.POST or None)
        # nesting_site_form = Submit_Species_Form_Nesting_Site(request.POST or None)
        
        if request.method =='POST':
          
            if species_form.is_valid():
            # and continent_form.is_valid() and country_form.is_valid() and order_form.is_valid() and family_form.is_valid() and micro_habitat_form.is_valid() and  activity_form.is_valid() and nesting_site_form.is_valid()
                
              
                submission = species_form.save(commit=False)
                submission.user = request.user
                submission.verif_status = False

                # continent_submit= continent_form.save(commit=False)
                # continent_submit.submission = submission

                # country_submit = country_form.save(commit=False)
                # country_submit.submission = submission

                # order_submit = order_form.save(commit=False)
                # order_submit.submission = submission

                # family_submit = family_form.save(commit=False)
                # family_submit.submission = submission

                # activity_submit = activity_form.save(commit=False)
                # activity_submit.submission = submission


                # micro_habitat_submit = micro_habitat_form.save(commit=False)  
                # micro_habitat_submit.species = submission
                # micro_habitat_submit.submission = submission

                # nesting_site_submit = nesting_site_form.save(commit=False)
                # nesting_site_submit.submission = submission

                submission.save()
             
                messages.success(request, ("Submission Successful Pending Approval"))
                return redirect('home:species_detail', submission.pk)
            
            else :
                messages.success(request, "Negative Value Entered For Positive Data Type")
                return redirect("home:submit_species")
        
        return render(request, 'home/account/submit_species.html', {'species_form':species_form,})

#  'continent_form' : continent_form, 'country_form' : country_form, 'order_form': order_form, 'family_form': family_form, 'micro_habitat_form':micro_habitat_form, 'activity_form':activity_form, 'nesting_site_form':nesting_site_form

class My_Submissions_List_View(ListView):
    paginate_by = 20
    model = Species
    template_name = "home/account/my_submissions.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(user=self.kwargs['user']).order_by('species_name_latin')
        

@login_required

def update_account_view(request):

     if request.method == "POST":
        user_form = User_Registration_Form(request.POST, instance=request.user)
        user_profile_form = User_Profile_Form(request.POST or None, request.FILES or None, instance=request.user.user_profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            messages.success(request, ("Update Successful"))

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("home:index")
     else:
        user_form = User_Registration_Form(instance=request.user)
        user_profile_form = User_Profile_Form(instance=request.user.user_profile)
        
        return render(request, "home/account/update_account.html", {"u_form":user_form, "p_form": user_profile_form})

class User_Profile_Detail_View (DetailView):
    model = User
    template_name = "home/account/profile_page.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile_list'] = User_Profile.objects.filter(user_id=context['object'].id)

        return context

##############################################Staff Views############################################################


def edit_species_view(request, species_id):
        species = Species.objects.get(species_id=species_id)
        species_form = Submit_Species_Form(request.POST or None, request.FILES or None, instance=species)
        # continent_form = Submit_Species_Form_Continent(request.POST or None)
        # country_form = Submit_Species_Form_Country_Geo_Location(request.POST or None)
        # order_form = Submit_Species_Form_Order(request.POST or None)
        # family_form = Submit_Species_Form_Family(request.POST or None)
        
        if request.method =='POST':
            if species_form.is_valid():
                # and continent_form.is_valid() and country_form.is_valid() and order_form.is_valid() and family_form.is_valid()
                submission = species_form.save(commit = False)
                submission.user = request.user

                # continent_submit= continent_form.save(commit=False)
                # continent_submit.submission = submission

                # country_submit = country_form.save(commit=False)
                # country_submit.submission = submission

                # order_submit = order_form.save(commit=False)
                # order_submit.submission = submission

                # family_submit = family_form.save(commit=False)
                # family_submit.submission = submission

                submission.save()
                messages.success(request, ("Species Updated"))
                return redirect('home:species_detail', submission.pk)
            
                
        return render(request, 'home/staff/edit_species.html',{'species': species,'species_form':species_form,})
#  'continent_form' : continent_form, 'country_form' : country_form, 'order_form': order_form, 'family_form': family_form


class Approve_Species_Update_View(UpdateView):
    
    model = Species
    template_name= "home/staff/approve_species.html"
    form_class = Approve_Species_Form

class Delete_Species_Delete_View(DeleteView):
    
    model = Species
    template_name= "home/staff/delete_species.html"
    success_url=reverse_lazy('home:index')



class Species_Unverified_List_View(ListView):
    
    paginate_by = 20
    model = Species
    template_name = "home/staff/unverified_species.html"
    context_object_name = 'species_list'


    def get_queryset(self):
        return Species.objects.filter(verif_status = False).order_by('species_name_latin')

        




#Used to identify correct dictionary keys when setting up filter searches for many-to-many filters
# for key, value in context.items() :
        #     print(f' key is {key} /// value is {value}')
        #print(self.kwargs)
        # print(dir(context['country_list']))
        # print('-----------------------')
        # country_new = Country.objects.filter(geo_location__geo_location_species__species_id__in='12')
        # print(country_new)
        # context['species_list'] = Species.objects.filter(nesting_site_species__nesting_site__nesting_site_id= self.kwargs['nesting_site_id'])

    
