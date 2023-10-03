import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *
import unittest

from django.views.generic import RedirectView

class Test_Urls(SimpleTestCase):


    #TU-01
    def test_index_url(self):
        url = reverse('home:index')
        print (resolve(url))
        self.assertEqual(resolve(url).func, index_view)

    #TU-02
    def test_iNaturalist_url(self):
        url = reverse('home:iNaturalist')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, RedirectView)

    #TU-03
    def test_data_summary_url(self):
        url = reverse('home:data_summary')
        print (resolve(url))
        self.assertEqual(resolve(url).func, data_summary_view)

    #TU-04
    def test_taxonomy_url(self):
        url = reverse('home:taxonomy')
        print (resolve(url))
        self.assertEqual(resolve(url).func, taxonomy_view)

    #TU-05
    def test_tax_order_url(self):
        url = reverse('home:tax_order')
        print (resolve(url))
        self.assertEqual(resolve(url).func, tax_order_view)

    #TU-06
    def test_tax_family_url(self):
        url = reverse('home:tax_family')
        print (resolve(url))
        self.assertEqual(resolve(url).func, tax_family_view)

    #TU-07
    def test_tax_genus_url(self):
        url = reverse('home:tax_genus')
        print (resolve(url))
        self.assertEqual(resolve(url).func, tax_genus_view)

    #TU-08
    def test_location_url(self):
        url = reverse('home:location')
        print (resolve(url))
        self.assertEqual(resolve(url).func, location_view)

    #TU-09
    def test_continent_url(self):
        url = reverse('home:loca_continent')
        print (resolve(url))
        self.assertEqual(resolve(url).func, loca_continent_view)

    #TU-10
    def test_country_url(self):
        url = reverse('home:loca_country')
        print (resolve(url))
        self.assertEqual(resolve(url).func, loca_country_view)

    #TU-11
    def test_micro_habitat_url(self):
        url = reverse('home:micro_habitat')
        print (resolve(url))
        self.assertEqual(resolve(url).func, micro_habitat_view)

    #TU-12
    def test_activity_url(self):
        url = reverse('home:activity')
        print (resolve(url))
        self.assertEqual(resolve(url).func, activity_view)

    #TU-13
    def test_population_trend_url(self):
        url = reverse('home:population_trend')
        print (resolve(url))
        self.assertEqual(resolve(url).func, population_trend_view)

    #TU-14
    def test_iucn_url(self):
        url = reverse('home:iucn')
        print (resolve(url))
        self.assertEqual(resolve(url).func, iucn_view)

    #TU-15
    def test_nesting_site_url(self):
        url = reverse('home:nesting_site')
        print (resolve(url))
        self.assertEqual(resolve(url).func, nesting_site_view)

    #TU-16
    def test_parity_mode_url(self):
        url = reverse('home:parity_mode')
        print (resolve(url))
        self.assertEqual(resolve(url).func, parity_mode_view)

    #TU-17
    def test_species_url(self):
        url = reverse('home:species')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_List_View)

    #TU-18
    def test_species_detail_url(self):
        url = reverse('home:species_detail', args='2')
        self.assertEqual(resolve(url).func.view_class, Species_Detail_Detail_View)

    #TU-19
    def test_search_species_url(self):
        url = reverse('home:search_species_latin')
        print (resolve(url))
        self.assertEqual(resolve(url).func, search_species_latin_name_view)

    #TU-20
    def test_species_parity_url(self):
        url = reverse('home:species_parity_mode', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Parity_List_View)

    #TU-21
    def test_species_pop_trend_url(self):
        url = reverse('home:species_pop_trend', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Pop_Trend_List_View)

    #TU-22
    def test_species_iucn_url(self):
        url = reverse('home:species_iucn', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Iucn_List_View)

    #TU-23
    def test_species_nesting_site_url(self):
        url = reverse('home:species_nesting_site', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Nesting_List_View)

    #TU-24
    def test_species_micro_habitat_url(self):
        url = reverse('home:species_micro_habitat', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Micro_Habitat_List_View)
  
    #TU-25
    def test_species_activity_url(self):
        url = reverse('home:species_activity', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Activity_List_View)

    #TU-26
    def test_species_country_url(self):
        url = reverse('home:species_country', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Country_List_View)

    #TU-27
    def test_species_continent_url(self):
        url = reverse('home:species_continent', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Continent_List_View)

    #TU-28
    def test_species_order_url(self):
        url = reverse('home:species_order', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Tax_Order_List_View)

    #TU-29
    def test_species_family_url(self):
        url = reverse('home:species_family', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Family_List_View)

    #TU-30
    def test_species_genus_url(self):
        url = reverse('home:species_genus', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Genus_List_View)

    #TU-31
    def test_my_page_url(self):
        url = reverse('home:mypage')
        print (resolve(url))
        self.assertEqual(resolve(url).func, my_page_view)

    #TU-32
    def test_profile_page_url(self):
        url = reverse('home:profile_page', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, User_Profile_Detail_View)

    #TU-33
    def test_update_account_url(self):
        url = reverse('home:update_account')
        print (resolve(url))
        self.assertEqual(resolve(url).func, update_account_view)

    #TU-34
    def test_my_submissions_url(self):
        url = reverse('home:my_submissions')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, My_Submissions_List_View)

    #TU-35
    def test_submit_species_url(self):
        url = reverse('home:submit_species')
        print (resolve(url))
        self.assertEqual(resolve(url).func, submit_species_view)

    #TU-36
    def test_edit_species_url(self):
        url = reverse('home:edit_species', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func, edit_species_view)

    #TU-37
    def test_approve_species_url(self):
        url = reverse('home:approve_species', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Approve_Species_Update_View)

    #TU-38
    def test_delete_species_url(self):
        url = reverse('home:delete_species', args='2')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Delete_Species_Delete_View)
  
    #TU-39
    def test_species_unverified_url(self):
        url = reverse('home:species_unverified')
        print (resolve(url))
        self.assertEqual(resolve(url).func.view_class, Species_Unverified_List_View)
    
    #TU-40
    def test_signup_url(self):
        url = reverse('home:signup')
        print (resolve(url))
        self.assertEqual(resolve(url).func, signup_view)

    #TU-41
    def test_login_user_url(self):
        url = reverse('home:login')
        print (resolve(url))
        self.assertEqual(resolve(url).func, login_user_view)
  
    #TU-42
    def test_logout_user_url(self):
        url = reverse('home:logout')
        print (resolve(url))
        self.assertEqual(resolve(url).func, logout_user_view)
    

   

    