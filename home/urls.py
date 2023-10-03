from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns = [
   
    path('', views.index_view, name='index'),
    path('iNaturalist', RedirectView.as_view(url='https://www.inaturalist.org/'), name = 'iNaturalist'),
    path('search/data_summary', views.data_summary_view, name='data_summary'),
    path('search/taxonomy', views.taxonomy_view, name='taxonomy'),
    path('search/tax_order', views.tax_order_view, name = 'tax_order'),
    path('search/tax_family', views.tax_family_view, name = 'tax_family'),
    path('search/tax_genus', views.tax_genus_view, name = 'tax_genus'),
    path('search/location', views.location_view, name='location'),
    path('search/loca_continent', views.loca_continent_view, name='loca_continent'),
    path('search/loca_country', views.loca_country_view, name='loca_country'),
    path('search/micro_habitat', views.micro_habitat_view, name='micro_habitat'),
    path('search/activity', views.activity_view, name='activity'),
    path('search/population_trend', views.population_trend_view, name='population_trend'),
    path('search/iucn', views.iucn_view, name='iucn'),
    path('search/nesting_site', views.nesting_site_view, name='nesting_site'),
    path('search/parity_mode', views.parity_mode_view, name='parity_mode'),
    path('search/species', views.Species_List_View.as_view(), name = 'species'),
    path('search/species/<int:pk>/', views.Species_Detail_Detail_View.as_view(), name = 'species_detail'),
    path('search/search_species/', views.search_species_latin_name_view, name = 'search_species_latin'),
    # path('search/search_species/', views.search_species_name_common_view, name = 'search_species_common'),
    path('search/species/parity_mode/<int:parity_mode_id>/', views.Species_Parity_List_View.as_view(), name='species_parity_mode'),
    path('search/species/pop_trend/<int:pop_trend_id>/', views.Species_Pop_Trend_List_View.as_view(), name='species_pop_trend'),
    path('search/species/iucn/<int:iucn_id>/', views.Species_Iucn_List_View.as_view(), name='species_iucn'),
    path('search/species/nesting_site/<int:nesting_site_id>/', views.Species_Nesting_List_View.as_view(), name='species_nesting_site'),
    path('search/species/micro_habitat/<int:micro_habitat_id>/', views.Species_Micro_Habitat_List_View.as_view(), name='species_micro_habitat'),
    path('search/species/activity/<int:activity_id>/', views.Species_Activity_List_View.as_view(), name='species_activity'),
    path('search/species/country/<int:country_id>/', views.Species_Country_List_View.as_view(), name='species_country'),
    path('search/species/continent/<int:continent_id>/', views.Species_Continent_List_View.as_view(), name='species_continent'),
    path('search/species/order/<int:order_id>/', views.Species_Tax_Order_List_View.as_view(), name='species_order'),
    path('search/species/family/<int:family_id>/', views.Species_Family_List_View.as_view(), name='species_family'),
    path('search/species/genus/<int:genus_id>/', views.Species_Genus_List_View.as_view(), name='species_genus'),
    path('account/mypage/', views.my_page_view, name = 'mypage'),
    path('account/profile_page/<int:pk>', views.User_Profile_Detail_View.as_view(), name = 'profile_page'),
    path('account/update_account/', views.update_account_view, name = 'update_account'),
    path('account/my_submissions/<int:user>', views.My_Submissions_List_View.as_view(), name = 'my_submissions'),
    path('account/submit_species/', views.submit_species_view, name = 'submit_species'),
    path('staff/edit_species/<int:species_id>', views.edit_species_view, name = 'edit_species'),
    path('staff/approve_species/<int:pk>', views.Approve_Species_Update_View.as_view(), name = 'approve_species'),
    path('staff/delete_species/<int:pk>', views.Delete_Species_Delete_View.as_view(), name = 'delete_species'),
    path('staff/species/unverified/', views.Species_Unverified_List_View.as_view(), name='species_unverified'),
    path('signup', views.signup_view, name = 'signup'),
    path('login_user', views.login_user_view, name = 'login'),
    path('logout_user', views.logout_user_view, name = 'logout'),
    path('staff/species_pdf_creator/<int:pk>', views.species_render_pdf_view, name='species_pdf_creator'),

    

    
]
