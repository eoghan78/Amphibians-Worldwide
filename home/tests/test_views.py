from django.contrib.messages import get_messages
from django.test.client import Client
from django.urls import reverse
import unittest
from home.views import *
from home.models import *
from django.contrib.auth.models import User
from home.tests.test_models import user_name_generator


class Test_Get_Views(unittest.TestCase):

    def setUp(self):
        # Setting up the user
        self.user = User.objects.create(username=user_name_generator())
        self.user_password_raw = 'secret78'
        self.user.set_password(self.user_password_raw)
        self.user.save()

        self.user_profile = User_Profile.objects.create(user=self.user)
        self.species = Species.objects.create(species_name_latin='species test', )
        self.parity_mode = Parity_Mode.objects.create(parity_mode_desc='parity test', )
        self.pop_trend = Pop_Trend.objects.create(pop_trend_status='pop trend test', )
        self.iucn = IUCN.objects.create(iucn_status='iucn test', )
        self.nesting_site = Nesting_Site.objects.create(nesting_site_desc='nesting site test', )
        self.micro_habitat = Micro_Habitat.objects.create(micro_habitat_name='microhabitat test')
        self.activity = Activity.objects.create(activity_kind='activity test')
        self.country = Country.objects.create(country_name='country test')
        self.continent = Continent.objects.create(continent_name='continent test')
        self.order_taxon = Order_Taxon.objects.create(order_taxon_name='order test')
        self.family = Family.objects.create(family_name='family test', order_id='1')
        self.genus = Genus.objects.create(genus_name='genus test', family_id='1')

        self.pdf_url = reverse('home:species_pdf_creator', args=[self.species.pk, ])
        self.index_url = reverse('home:index')
        self.data_summary_url = reverse('home:data_summary')
        self.location_url = reverse('home:location')
        self.continent_url = reverse('home:loca_continent')
        self.country_url = reverse('home:loca_country')
        self.micro_habitat_url = reverse('home:micro_habitat')
        self.activity_url = reverse('home:activity')
        self.pop_trend_url = reverse('home:population_trend')
        self.iucn_url = reverse('home:iucn')
        self.nesting_site_url = reverse('home:nesting_site')
        self.parity_mode_url = reverse('home:parity_mode')
        self.taxonomy_url = reverse('home:taxonomy')
        self.tax_order_url = reverse('home:tax_order')
        self.tax_family_url = reverse('home:tax_family')
        self.tax_genus_url = reverse('home:tax_genus')
        self.species_url = reverse('home:species')
        self.species_parity_url = reverse('home:species_parity_mode', args=[self.parity_mode.parity_mode_id, ])
        self.species_pop_trend_url = reverse('home:species_pop_trend', args=[self.pop_trend.pop_trend_id, ])
        self.species_iucn_url = reverse('home:species_iucn', args=[self.iucn.iucn_id, ])
        self.species_nesting_site_url = reverse('home:species_nesting_site', args=[self.nesting_site.nesting_site_id, ])
        self.species_micro_habitat_url = reverse('home:species_micro_habitat', args=[self.micro_habitat.micro_habitat_id, ])
        self.species_activity_url = reverse('home:species_activity', args=[self.activity.activity_id, ])
        self.species_country_url = reverse('home:species_country', args=[self.country.country_id, ])
        self.species_continent_url = reverse('home:species_continent', args=[self.continent.continent_id, ])
        self.species_tax_order_url = reverse('home:species_order', args=[self.order_taxon.order_id, ])
        self.species_family_url = reverse('home:species_family', args=[self.family.family_id, ])
        self.species_genus_url = reverse('home:species_genus', args=[self.genus.genus_id, ])
        self.species_detail_url = reverse('home:species_detail', args=[self.species.pk, ])
        self.mypage_url = reverse('home:mypage')
        self.my_submissions_url = reverse('home:my_submissions')
        self.user_profile_url = reverse('home:profile_page', args=[self.user.pk, ])
        self.approve_species_url = reverse('home:approve_species', args=[self.species.pk, ])
        self.delete_species_url = reverse('home:delete_species', args=[self.species.pk, ])
        self.species_unver_url = reverse('home:species_unverified')
        self.login_url = reverse('home:login')
        self.logout_url = reverse('home:logout')

        self.client = Client()


    ##################################################Views######################################################################

    #TV-01
    def test_species_render_pdf_view(self):
        
        response = self.client.get(self.pdf_url)
        self.assertEqual(response.status_code, 200)


    #TV-02
    def test_index_view_Get(self):

        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)

    #TV-03
    def test_data_summary_view_Get(self):
        
        response = self.client.get(self.data_summary_url)
        self.assertEqual(response.status_code, 200)

##########################################################Variable Views#######################################################

    #TV-04
    def test_location_view_Get(self):
        
        response = self.client.get(self.location_url)
        self.assertEqual(response.status_code, 200)

    #TV-05
    def test_continent_view_Get(self):

        response = self.client.get(self.continent_url)
        self.assertEqual(response.status_code, 200)

    #TV-06
    def test_country_view_Get(self):

        response = self.client.get(self.country_url)
        self.assertEqual(response.status_code, 200)

    #TV-07
    def test_micro_habitat_view_Get(self):

        response = self.client.get(self.micro_habitat_url)
        self.assertEqual(response.status_code, 200)

    #TV-08
    def test_activity_view_Get(self):

        response = self.client.get(self.activity_url)
        self.assertEqual(response.status_code, 200)

    #TV-09
    def test_pop_trend_view_Get(self):

        response = self.client.get(self.pop_trend_url)
        self.assertEqual(response.status_code, 200)

    #TV-10
    def test_iucn_view_Get(self):

        response = self.client.get(self.iucn_url)
        self.assertEqual(response.status_code, 200)

    #TV-11
    def test_nesting_site_view_Get(self):

        response = self.client.get(self.nesting_site_url)
        self.assertEqual(response.status_code, 200)

    #TV-12
    def test_parity_mode_view_Get(self):

        response = self.client.get(self.parity_mode_url)
        self.assertEqual(response.status_code, 200)

    #TV-13
    def test_taxonomy_view_Get(self):

        response = self.client.get(self.taxonomy_url)
        self.assertEqual(response.status_code, 200)

    #TV-14
    def test_tax_order_view_Get(self):

        response = self.client.get(self.tax_order_url)
        self.assertEqual(response.status_code, 200)

    #TV-15
    def test_tax_family_view_Get(self):

        response = self.client.get(self.tax_family_url)
        self.assertEqual(response.status_code, 200)

    #TV-16
    def test_tax_genus_view_Get(self):

        response = self.client.get(self.tax_genus_url)
        self.assertEqual(response.status_code, 200)

####################################################Species Related Tests#########################################################

    #TV-17
    def test_Species_List_View_Get(self):

        response = self.client.get(self.species_url)
        self.assertEqual(response.status_code, 200)

    #TV-18
    def test_Species_Detail_Detail_View_Get(self):

        response = self.client.get(self.species_detail_url)
        self.assertEqual(response.status_code, 200)

    #TV-19
    # Assert the context returned in the response contains the species data
    def test_Species_Detail_Detail_View_in_context(self):
        response = self.client.get(self.species_detail_url, {'pk': self.species.species_id})       
        self.assertEqual(response.context['species_list'], self.species)
        self.assertEqual(response.status_code, 200)


######################################################Species filter views########################################################

#####################################################One to Many##################################################################
    #TV-20
    def test_Species_Parity_List_View_Get(self):
        
        response = self.client.get(self.species_parity_url)
        self.assertEqual(response.status_code, 200)

    #TV-21
    def test_Species_Pop_Trend_List_View_Get(self):

        response = self.client.get(self.species_pop_trend_url)
        self.assertEqual(response.status_code, 200)

    #TV-22
    def test_Species_Iucn_List_View_Get(self):

        response = self.client.get(self.species_iucn_url)
        self.assertEqual(response.status_code, 200)

    #######################################################Many to Many###########################################################

    #TV-23
    def test_Species_Nesting_List_View_Get(self):

        response = self.client.get(self.species_nesting_site_url)
        self.assertEqual(response.status_code, 200)

    #TV-24
    def test_Micro_Habitat_List_View_Get(self):

        response = self.client.get(self.species_micro_habitat_url)
        self.assertEqual(response.status_code, 200)

    #TV-25
    def test_Species_Activity_List_View_Get(self):

        response = self.client.get(self.species_activity_url)
        self.assertEqual(response.status_code, 200)

    #######################################################Hierarchical Views####################################################

    #TV-26
    def test_Species_Country_List_View_Get(self):

        response = self.client.get(self.species_country_url)
        self.assertEqual(response.status_code, 200)

    #TV-27
    def test_Species_Continent_List_View_Get(self):

        response = self.client.get(self.species_continent_url)
        self.assertEqual(response.status_code, 200)

    #TV-28
    def test_Species_Tax_Order_List_View_Get(self):

        response = self.client.get(self.species_tax_order_url)
        self.assertEqual(response.status_code, 200)

    #TV-29
    def test_Species_Family_List_View_Get(self):

        response = self.client.get(self.species_family_url)
        self.assertEqual(response.status_code, 200)

    #TV-30
    def test_Species_Genus_List_View_Get(self):

        response = self.client.get(self.species_genus_url)
        self.assertEqual(response.status_code, 200)

    ####################################Sign up and Login/LogoutViews####################################################

    #TV-31
    def test_login_user_view_success(self):


        login_details = {'username': self.user.username,
                         'password': 'secret78'}

        response = self.client.post(self.login_url, data=login_details, follow=True)
        response_message = list(get_messages(response.wsgi_request))

        print(str(response_message[0]))

        self.assertEqual(str(response_message[0]), 'Logged In')
        self.assertEqual(response.status_code, 200)

    #TV-32
    def test_login_user_view_fail(self):

        login_details = {'username': self.user.username,
                         'password': 'wrong password'}

        response = self.client.post(self.login_url, data=login_details, follow=True)
        response_message = list(get_messages(response.wsgi_request))

        self.assertEqual(str(response_message[0]), 'Incorrect username or password')
        self.assertEqual(response.status_code, 200)

    #TV-33
    def test_logout_user_view(self):
        client=Client()
        response = client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)

    ###############################################User Views############################################################

    #TV-34
    def test_my_page_view_Get(self):

        response = self.client.get(self.mypage_url)
        self.assertEqual(response.status_code, 200)

    #TV-35
    def test_My_Submissions_List_View_Get(self):
       
        response = self.client.get(self.my_submissions_url)
        self.assertEqual(response.status_code, 200)


    #TV-36
    def test_User_Profile_Detail_View_Get(self):
       
        response = self.client.get(self.user_profile_url)
        self.assertEqual(response.status_code, 200)

    ##############################################Staff Views############################################################



    #TV-37
    def test_Approve_Species_Update_View_Get(self):
        client=Client()
        response = client.get(self.approve_species_url)
        self.assertEqual(response.status_code, 200)

    #TV-38
    def test_Delete_Species_Delete_View_Get(self):
        client=Client()
        response = client.get(self.delete_species_url)
        self.assertEqual(response.status_code, 200)

    #TV-39
    def test_Species_Unverified_List_View_Get(self):
        client=Client()
        response = client.get(self.species_unver_url)
        self.assertEqual(response.status_code, 200)